using CSharpClientExample;
using Google.Protobuf.Collections;
using Grpc.Core;
using Grpc.Net.Client;
using SuperBuilderWinService;
using Newtonsoft.Json;

var grpcServerAddress = "http://localhost:5006";

Console.WriteLine("Creating connection to SuperBuilder middleware (AssistantService)...");


var httpClientHandler = new HttpClientHandler
{
    UseProxy = false, // Disable the proxy
    SslProtocols = System.Security.Authentication.SslProtocols.Tls12 | System.Security.Authentication.SslProtocols.Tls13,
    ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator // For development only
};

// Create the HttpClient with the handler
var httpClient = new HttpClient(httpClientHandler)
{
    DefaultRequestVersion = new Version(2, 0),
    DefaultVersionPolicy = HttpVersionPolicy.RequestVersionOrHigher
};

// Create the GrpcChannel with the HttpClient
var channel = GrpcChannel.ForAddress(grpcServerAddress, new GrpcChannelOptions
{
    HttpClient = httpClient,
    Credentials = ChannelCredentials.Insecure // Use Insecure for local development
});



//using var channel = GrpcChannel.ForAddress("http://localhost:5006");
var client = new SuperBuilder.SuperBuilderClient(channel);

Console.WriteLine("\n\n-------- Say Hello Test -------");

// Make a gRPC call
try
{
    var sayHelloResponse = await client.SayHelloAsync(new SayHelloRequest { Name = "SuperBuilder C# Client!" });
    Console.WriteLine("Server Reply: " + sayHelloResponse.Message);
}
catch (RpcException e)
{
    Console.WriteLine($"gRPC error: {e.Status.Detail}");
}
catch (HttpRequestException e)
{
    Console.WriteLine($"HTTP request error: {e.Message}");
}


Console.WriteLine("\n\n-------- Get Software Update ------- ");
var updateResponse = await client.GetSoftwareUpdateAsync(new SayHelloRequest { Name = "SuperBuilder C# Client!" });
Console.WriteLine("Server Reply: " + updateResponse.Message);

Console.WriteLine("\n\n-------- Health Check Test -------");
var checkHealthResponse = await client.CheckHealthAsync(new CheckHealthRequest { TypeOfCheck = "RAG" });
Console.WriteLine("\nServer Reply: " + checkHealthResponse.Status);



// CHAT TEST
Console.WriteLine("\n\n-------- Chat Test -------");
var chatRequest = new ChatRequest
{
    Name = "SuperBuilder C# Client!",
    Prompt = "What were we just talking about?",
};
// add in some chat history
chatRequest.History.Add(new ConversationHistory { Role = "user", Content = "Tell me a bit about yourself" });
chatRequest.History.Add(new ConversationHistory { Role = "assistant", Content = "I am an Intel AI Assistant, a chatbot developed by Intel. I can help you with various tasks provided context." });
var fullResponse = "";
try
{
    // // Set a timeout of 10 seconds (For testing)
    // var callOptions = new CallOptions(deadline: DateTime.UtcNow.AddSeconds(5));
    var r = client.Chat(chatRequest);
    await foreach (var response in r.ResponseStream.ReadAllAsync())
    {
        Console.WriteLine("Received chat message: " + response.Message);
        // convert response.Message to json
        var messageDict = JsonConvert.DeserializeObject<Dictionary<string, string>>(response.Message);
        messageDict.TryGetValue("message", out var messageValue);
        fullResponse += messageValue;
    }
}
catch (Exception ex)
{
    Console.WriteLine($"Unexpected error: {ex.Message}");
    Console.WriteLine($"Sending stop generation now...");
    var stopRequest = new StopChatRequest { };
    var stopResponse = client.StopChat(stopRequest);
    Console.WriteLine($"Generation stopped");
}
finally
{
    Console.WriteLine($"Full response: {fullResponse}");
}