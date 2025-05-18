using Newtonsoft.Json;
using Grpc.Core;
using Grpc.Net.Client;
using SuperBuilderWinService;


namespace CSharpClientExample
{
    public static class Benchmark
    {
        private class TestStep
        {
            public string? Type { get; set; }
            public string[]? Files { get; set; }
            public string? Content { get; set; }
        }

        private class TestStepsFile
        {
            public string? TestName { get; set; }
            public string? MetricOutputFilePath { get; set; }
            public string[]? ModelList { get; set; }
            public List<TestStep>? TestSteps { get; set; }
        }

        private static TestStepsFile ParseJSONFile(string fileName)
        {
            string filePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Tests", fileName);
            string jsonString = File.ReadAllText(filePath);
            TestStepsFile? testFile = JsonConvert.DeserializeObject<TestStepsFile>(jsonString);
            if (testFile == null || testFile.TestSteps == null)
            {
                throw new Exception($"Could not read JSON file {filePath}");
            }
            return testFile;
        }

        /// <summary>
        /// Parse a test file and execute all test steps by calling the middleware APIs via grpc
        /// (Middleware and Backend must be running for this to work)
        /// 
        /// Metrics will output to specified file path in JSON test file MetricOutputFilePath field
        /// </summary>
        /// <param name="fileName">The JSON file with the test steps, should be added to the build to use</param>
        public static async Task ExecuteTestOnFile(string fileName)
        {
            // Connect to the middleware
            using var channel = GrpcChannel.ForAddress("http://localhost:5006");
            var client = new SuperBuilder.SuperBuilderClient(channel);

            // Get the test execution steps from the JSON file
            TestStepsFile testFile = ParseJSONFile(fileName);

            Console.WriteLine($"\n\n\n=====================================================================================");
            Console.WriteLine($"Running {testFile.TestName}, outputting results to C:\\temp\\IntelAia\\generation.metrics.csv");
            Console.WriteLine($"=====================================================================================\n\n\n");

            foreach (string modelPath in testFile.ModelList)
            {
                Console.WriteLine($"--------------Running on Model: {modelPath}----------------\n\n");
                await client.SetModelsAsync(new SetModelsRequest { Llm = modelPath, 
                                                        Embedder = "local_models\\bge-base-en-v1.5-int8-ov",
                                                        Ranker = "local_models\\bge-reranker-base-int8-ov",
                                                        });

                // Execute each test step in order
                foreach (TestStep testStep in testFile.TestSteps)
                {
                    // Parse what type of API to call through Test Type, which will determine the contents of the test step
                    Console.WriteLine($"\n\nExecuting test step: {testStep.Type}");
                    switch (testStep.Type)
                    {
                        case "Chat":
                            Console.WriteLine($"Calling Chat with Prompt: {testStep.Content}...");
                            string formatDate = DateTime.Now.ToString("yyyyMMdd");
                            string fixedOutputPath = $"C:\\temp\\IntelAia\\{formatDate}.generation.metrics.csv";
                            var chatResponse = client.Chat(new ChatRequest { Name = "SuperBuilder C# Client!", Prompt = testStep.Content});
                            string result = "";
                            try
                            {
                                await foreach (var response in chatResponse.ResponseStream.ReadAllAsync())
                                {
                                    result += response.Message;
                                }
                                Console.WriteLine($"Output to: {fixedOutputPath}...");
                            }
                            catch (Exception e)
                            {
                                Console.WriteLine(e.ToString());
                            }
                            Console.WriteLine("\nServer Reply: " + result);
                            break;
                        case "AddFiles":
                            Console.WriteLine($"Calling AddFiles with FilesToUpload: [{String.Join(", ", testStep.Files)}]...");
                            var grpcUploadList = JsonConvert.SerializeObject(testStep.Files);
                            var addFileResponse = client.AddFiles(new AddFilesRequest { FilesToUpload = grpcUploadList });
                            Console.WriteLine("\nServer Reply: " + addFileResponse.ToString());
                            break;
                        case "RemoveFiles":
                            Console.WriteLine($"Calling RemoveFiles with FilesToRemove: [{String.Join(", ", testStep.Files)}]...");
                            var grpcRemoveList = JsonConvert.SerializeObject(testStep.Files);
                            var removeFilesResponse = await client.RemoveFilesAsync(new RemoveFilesRequest { FilesToRemove = grpcRemoveList });
                            Console.WriteLine("\nServer Reply: " + removeFilesResponse.FilesRemoved);
                            break;
                        case "SayHello":
                            Console.WriteLine($"Calling SayHello with Name: {testStep.Content}...");
                            var sayHelloResponse = await client.SayHelloAsync(new SayHelloRequest { Name = testStep.Content });
                            Console.WriteLine("Server Reply: " + sayHelloResponse.Message);
                            break;
                        case "CheckHealth":
                            Console.WriteLine($"Calling CheckHealth with Type of Check: {testStep.Content}...");
                            var checkHealthResponse = await client.CheckHealthAsync(new CheckHealthRequest { TypeOfCheck = testStep.Content });
                            Console.WriteLine("\nServer Reply: " + checkHealthResponse.Status);
                            break;
                        case "AddFeedback":
                            Console.WriteLine($"Calling AddFeedback with Feedback Comment: {testStep.Content}...");
                            break;
                        case "GetFileList":
                            Console.WriteLine($"Calling GetFileList...");
                            var getFileResponse = await client.GetFileListAsync(new GetFileListRequest { FileType = "" });
                            Console.WriteLine("\nServer Reply: " + getFileResponse.FileList);
                            break;
                        default:
                            throw new Exception($"Could not recognize test step {testStep.Type}...");
                    }
                }
                Console.WriteLine($"{modelPath} TEST COMPLETE.");
            }
            Console.WriteLine($"ALL TESTS COMPLETE.");
        }
    }
}