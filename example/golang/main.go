package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"math/rand"
	"time"

	middleware "superbuilder/proto"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	serverAddress := "localhost:5006"
	fmt.Println("connecting to server at", serverAddress)

	conn, err := grpc.NewClient(serverAddress, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	// middlewareClient responsible for communicating with the server
	middlewareClient := middleware.NewSuperBuilderClient(conn)

	// create default context to manage the connection timeout
	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()

	// create longer context to manage the connection timeout
	// this is to compensate for the long running functions, e.g. SetParameters
	ctx_no_timeout := context.Context(context.Background())

	// ------------------ example of calling server ------------------

	// example 1 - call server and return system information
	fmt.Println("\n\nexample 1 - call server and return system information")
	fmt.Println("==========")
	responseSayHello, err := middlewareClient.SayHello(ctx, &middleware.SayHelloRequest{})
	if err != nil {
		log.Fatalf("error calling function SayHello: %v", err)
	}
	fmt.Println(responseSayHello.GetMessage())

	// example 2 - call server and return chat history
	fmt.Println("\n\nexample 2 - call server and return chat history")
	fmt.Println("==========")
	responseGetChatHistory, err := middlewareClient.GetChatHistory(ctx_no_timeout, &middleware.GetChatHistoryRequest{})
	if err != nil {
		log.Fatalf("error calling function GetChatHistory: %v", err)
	}
	fmt.Println(responseGetChatHistory.GetData())

	// example 3 - get current client model configuration
	fmt.Println("\n\nexample 3 - call server and return client model configuration")
	fmt.Println("==========")
	responseGetClientConfig, err := middlewareClient.GetClientConfig(ctx, &middleware.GetClientConfigRequest{})
	if err != nil {
		log.Fatalf("error calling function GetClientConfig: %v", err)
	}
	// fmt.Println(responseGetClientConfig.GetData())

	// unmarshal json
	var f interface{}
	err = json.Unmarshal([]byte(responseGetClientConfig.Data), &f)
	if err != nil {
		log.Fatalf("error unmarshalling client config: %v", err)
	}

	currentUserConfig := f.(map[string]interface{})
	ActiveAssistant := currentUserConfig["ActiveAssistant"].(map[string]interface{})
	selectedModels := ActiveAssistant["models"]
	AllModels := ActiveAssistant["all_models"].([]interface{})

	// show activeAssistant Model configuration
	var embedding_model map[string]interface{}
	var ranker_model map[string]interface{}
	var chat_model map[string]interface{}

	for _, each := range selectedModels.([]interface{}) {
		current := each.(map[string]interface{})
		if current["model_type"] == "chat_model" {
			chat_model = current
		}
		if current["model_type"] == "embedding_model" {
			embedding_model = current
		}
		if current["model_type"] == "ranker_model" {
			ranker_model = current
		}
	}
	fmt.Println("current embedding model:", embedding_model["full_name"])
	fmt.Println("current ranker model:", ranker_model["full_name"])
	fmt.Println("current chat model:", chat_model["full_name"])

	// example 4 - change active chat model
	fmt.Println("\n\nexample 4 - change active chat model")
	fmt.Println("==========")

	next_chat_model := "Qwen2-7B-Instruct-int4"
	if chat_model["full_name"] == "Qwen2-7B-Instruct-int4" {
		next_chat_model = "Phi-3-mini-4k-instruct-int4-ov"
	}

	// all chat models
	for _, each := range AllModels {
		current := each.(map[string]interface{})
		if current["full_name"] == next_chat_model {
			chat_model = current
		}
	}

	fmt.Println("changing current chat model to:", chat_model["full_name"])

	var newModelsConfiguration []map[string]interface{}
	newModelsConfiguration = append(newModelsConfiguration, embedding_model)
	newModelsConfiguration = append(newModelsConfiguration, ranker_model)
	newModelsConfiguration = append(newModelsConfiguration, chat_model)

	ModelsJsonFormat, err := json.Marshal(newModelsConfiguration)
	if err != nil {
		log.Fatalf("error marshalling new models configuration: %v", err)
	}
	middlewareClient.SetActiveAssistant(ctx_no_timeout, &middleware.SetActiveAssistantRequest{
		Assistant:  ActiveAssistant["short_name"].(string),
		ModelsJson: string(ModelsJsonFormat),
	})

	// example 5 - chat with the server
	fmt.Println("\n\nexample 5 - chat with the server")
	fmt.Println("==========")
	type ChatResponseInJSON struct {
		Message string `json:"message"`
	}

	var attachedFiles string = "[]"
	var randomInt int32 = rand.Int31()

	var questions []string = []string{
		"what is the model name of the current chat model?",
		"what is the model name of the current embedding model?",
		"what is the model name of the current reranker model?",
		"why the sky blue?",
		"why the sea purple?",
		"why the tree leaf green?",
	}

	middlewareChatRequest := middleware.ChatRequest{
		Name:          "SuperBuilder Go Clients!",
		Prompt:        questions[rand.Intn(len(questions))],
		SessionId:     randomInt, // random number to identify the session
		AttachedFiles: &attachedFiles,
	}

	fmt.Println("Question:\n", middlewareChatRequest.Prompt)
	responseHandler, err := middlewareClient.Chat(ctx_no_timeout, &middlewareChatRequest)
	if err != nil {
		log.Fatalf("error calling function Chat: %v", err)
	}

	fullMessage := ""
	for {
		chatResponse, err := responseHandler.Recv()
		if err == io.EOF {
			// End of stream reached
			// log.Println("Stream ended by server")
			break
		}
		if err != nil {
			_, err2 := middlewareClient.StopChat(ctx_no_timeout, &middleware.StopChatRequest{})
			if err2 != nil {
				log.Fatalf("error calling function StopChat: %v", err2)
			}
			fmt.Println("Chat stopped successfully")
			log.Fatalf("error receiving chat response: %v", err)
		}

		var message ChatResponseInJSON
		messageObject := chatResponse.GetMessage()
		json.Unmarshal([]byte(messageObject), &message)
		fullMessage += message.Message
		fmt.Print(message.Message)
	}

	fmt.Println("\n\n\n### Golang example ended ###")

}
