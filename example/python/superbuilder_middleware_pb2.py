# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: superbuilder_middleware.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'superbuilder_middleware.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsuperbuilder_middleware.proto\x12\x0cSuperBuilder\"\x1f\n\x0fSayHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"#\n\x10SayHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"4\n\x13\x43onversationHistory\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\xc6\x01\n\x0b\x43hatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x32\n\x07history\x18\x03 \x03(\x0b\x32!.SuperBuilder.ConversationHistory\x12\x11\n\tsessionId\x18\x04 \x01(\x05\x12\x16\n\tqueryType\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rattachedFiles\x18\x06 \x01(\tH\x01\x88\x01\x01\x42\x0c\n\n_queryTypeB\x10\n\x0e_attachedFiles\"\x1f\n\x0c\x43hatResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x11\n\x0fStopChatRequest\"\x12\n\x10StopChatResponse\"\x13\n\x11LoadModelsRequest\"$\n\x12LoadModelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\")\n\x12\x43heckHealthRequest\x12\x13\n\x0btypeOfCheck\x18\x01 \x01(\t\"%\n\x13\x43heckHealthResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"n\n\x12\x41\x64\x64\x46\x65\x65\x64\x62\x61\x63kRequest\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x10\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x65\x64\x62\x61\x63kType\x18\x03 \x01(\t\x12\x13\n\x06\x61nswer\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_answer\"&\n\x13\x41\x64\x64\x46\x65\x65\x64\x62\x61\x63kResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"(\n\x0f\x41\x64\x64\x46ilesRequest\x12\x15\n\rfilesToUpload\x18\x01 \x01(\t\"\x9f\x01\n\x10\x41\x64\x64\x46ilesResponse\x12\x15\n\rfilesUploaded\x18\x01 \x01(\t\x12!\n\x14\x63urrentFileUploading\x18\x02 \x01(\tH\x00\x88\x01\x01\x12 \n\x13\x63urrentFileProgress\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x17\n\x15_currentFileUploadingB\x16\n\x14_currentFileProgress\"&\n\x12GetFileListRequest\x12\x10\n\x08\x66ileType\x18\x01 \x01(\t\"\x15\n\x13StopAddFilesRequest\"\x16\n\x14StopAddFilesResponse\"\x1b\n\x19\x43lientDisconnectedRequest\"\'\n\x13GetFileListResponse\x12\x10\n\x08\x66ileList\x18\x01 \x01(\t\"+\n\x12RemoveFilesRequest\x12\x15\n\rfilesToRemove\x18\x01 \x01(\t\"+\n\x13RemoveFilesResponse\x12\x14\n\x0c\x66ilesRemoved\x18\x01 \x01(\t\"\\\n\x14\x44ownloadFilesRequest\x12\x0f\n\x07\x46ileUrl\x18\x01 \x01(\t\x12\x11\n\tlocalPath\x18\x02 \x01(\t\x12\x14\n\x07tokenId\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_tokenId\"A\n\x15\x44ownloadFilesResponse\x12\x10\n\x08progress\x18\x01 \x01(\x05\x12\x16\n\x0e\x46ileDownloaded\x18\x02 \x01(\t\"p\n\x10SetModelsRequest\x12\x10\n\x03llm\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x65mbedder\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06ranker\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x06\n\x04_llmB\x0b\n\t_embedderB\t\n\x07_ranker\")\n\x11SetModelsResponse\x12\x14\n\x0cmodelsLoaded\x18\x01 \x01(\t\"D\n\x13UnloadModelsRequest\x12\x0b\n\x03llm\x18\x01 \x01(\x08\x12\x10\n\x08\x65mbedder\x18\x02 \x01(\x08\x12\x0e\n\x06ranker\x18\x03 \x01(\x08\".\n\x14UnloadModelsResponse\x12\x16\n\x0emodelsUnloaded\x18\x01 \x01(\t\"/\n\x14SetParametersRequest\x12\x17\n\x0fparameters_json\x18\x01 \x01(\t\"\x17\n\x15SetParametersResponse\"\x1c\n\x1a\x43lientDisconnectedResponse\"+\n\x16GetClientConfigRequest\x12\x11\n\tassistant\x18\x01 \x01(\t\"\'\n\x17GetClientConfigResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x17\n\x15GetChatHistoryRequest\"&\n\x16GetChatHistoryResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\".\n\x12SetVectorDBRequest\x12\x18\n\x10\x63onnectionString\x18\x01 \x01(\t\"&\n\x13SetVectorDBResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\")\n\x14RemoveSessionRequest\x12\x11\n\tsessionId\x18\x01 \x01(\x05\"(\n\x15RemoveSessionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"?\n\x15SetSessionNameRequest\x12\x11\n\tsessionId\x18\x01 \x01(\x05\x12\x13\n\x0bsessionName\x18\x02 \x01(\t\")\n\x16SetSessionNameResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"C\n\x19SetActiveAssistantRequest\x12\x11\n\tassistant\x18\x01 \x01(\t\x12\x13\n\x0bmodels_json\x18\x02 \x01(\t\">\n\x1aSetActiveAssistantResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"K\n\x1cSetAssistantViewModelRequest\x12\x12\n\nview_model\x18\x01 \x01(\t\x12\x17\n\x0fresetUXSettings\x18\x02 \x01(\x08\"0\n\x1dSetAssistantViewModelResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"3\n\x1dSetUserConfigViewModelRequest\x12\x12\n\nview_model\x18\x01 \x01(\t\"1\n\x1eSetUserConfigViewModelResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"Q\n\x13\x43onvertModelRequest\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12\x17\n\nparameters\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_parameters\"\'\n\x14\x43onvertModelResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"z\n\x12UploadModelRequest\x12\x12\n\nsource_dir\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x12\n\nmodel_type\x18\x03 \x01(\t\x12\x15\n\rdownload_link\x18\x04 \x01(\t\x12\x16\n\x0emove_directory\x18\x05 \x01(\x08\"&\n\x13UploadModelResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"D\n\x17\x45xportUserConfigRequest\x12\x15\n\rAssistantName\x18\x01 \x01(\t\x12\x12\n\nExportPath\x18\x02 \x01(\t\"<\n\x18\x45xportUserConfigResponse\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x0f\n\x07Message\x18\x02 \x01(\t\"-\n\x17ImportUserConfigRequest\x12\x12\n\nImportPath\x18\x01 \x01(\t\"<\n\x18ImportUserConfigResponse\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x0f\n\x07Message\x18\x02 \x01(\t2\x9b\x14\n\x0cSuperBuilder\x12I\n\x08SayHello\x12\x1d.SuperBuilder.SayHelloRequest\x1a\x1e.SuperBuilder.SayHelloResponse\x12N\n\rSayHelloPyllm\x12\x1d.SuperBuilder.SayHelloRequest\x1a\x1e.SuperBuilder.SayHelloResponse\x12?\n\x04\x43hat\x12\x19.SuperBuilder.ChatRequest\x1a\x1a.SuperBuilder.ChatResponse0\x01\x12I\n\x08StopChat\x12\x1d.SuperBuilder.StopChatRequest\x1a\x1e.SuperBuilder.StopChatResponse\x12O\n\nLoadModels\x12\x1f.SuperBuilder.LoadModelsRequest\x1a .SuperBuilder.LoadModelsResponse\x12R\n\x0b\x43heckHealth\x12 .SuperBuilder.CheckHealthRequest\x1a!.SuperBuilder.CheckHealthResponse\x12R\n\x0b\x41\x64\x64\x46\x65\x65\x64\x62\x61\x63k\x12 .SuperBuilder.AddFeedbackRequest\x1a!.SuperBuilder.AddFeedbackResponse\x12K\n\x08\x41\x64\x64\x46iles\x12\x1d.SuperBuilder.AddFilesRequest\x1a\x1e.SuperBuilder.AddFilesResponse0\x01\x12U\n\x0cStopAddFiles\x12!.SuperBuilder.StopAddFilesRequest\x1a\".SuperBuilder.StopAddFilesResponse\x12R\n\x0bRemoveFiles\x12 .SuperBuilder.RemoveFilesRequest\x1a!.SuperBuilder.RemoveFilesResponse\x12Z\n\rDownloadFiles\x12\".SuperBuilder.DownloadFilesRequest\x1a#.SuperBuilder.DownloadFilesResponse0\x01\x12R\n\x0bGetFileList\x12 .SuperBuilder.GetFileListRequest\x1a!.SuperBuilder.GetFileListResponse\x12L\n\tSetModels\x12\x1e.SuperBuilder.SetModelsRequest\x1a\x1f.SuperBuilder.SetModelsResponse\x12U\n\x0cUnloadModels\x12!.SuperBuilder.UnloadModelsRequest\x1a\".SuperBuilder.UnloadModelsResponse\x12X\n\rSetParameters\x12\".SuperBuilder.SetParametersRequest\x1a#.SuperBuilder.SetParametersResponse\x12g\n\x12\x43lientDisconnected\x12\'.SuperBuilder.ClientDisconnectedRequest\x1a(.SuperBuilder.ClientDisconnectedResponse\x12^\n\x0fGetClientConfig\x12$.SuperBuilder.GetClientConfigRequest\x1a%.SuperBuilder.GetClientConfigResponse\x12[\n\x0eGetChatHistory\x12#.SuperBuilder.GetChatHistoryRequest\x1a$.SuperBuilder.GetChatHistoryResponse\x12R\n\x11GetSoftwareUpdate\x12\x1d.SuperBuilder.SayHelloRequest\x1a\x1e.SuperBuilder.SayHelloResponse\x12R\n\x0bSetVectorDB\x12 .SuperBuilder.SetVectorDBRequest\x1a!.SuperBuilder.SetVectorDBResponse\x12X\n\rRemoveSession\x12\".SuperBuilder.RemoveSessionRequest\x1a#.SuperBuilder.RemoveSessionResponse\x12[\n\x0eSetSessionName\x12#.SuperBuilder.SetSessionNameRequest\x1a$.SuperBuilder.SetSessionNameResponse\x12g\n\x12SetActiveAssistant\x12\'.SuperBuilder.SetActiveAssistantRequest\x1a(.SuperBuilder.SetActiveAssistantResponse\x12p\n\x15SetAssistantViewModel\x12*.SuperBuilder.SetAssistantViewModelRequest\x1a+.SuperBuilder.SetAssistantViewModelResponse\x12s\n\x16SetUserConfigViewModel\x12+.SuperBuilder.SetUserConfigViewModelRequest\x1a,.SuperBuilder.SetUserConfigViewModelResponse\x12U\n\x0c\x43onvertModel\x12!.SuperBuilder.ConvertModelRequest\x1a\".SuperBuilder.ConvertModelResponse\x12R\n\x0bUploadModel\x12 .SuperBuilder.UploadModelRequest\x1a!.SuperBuilder.UploadModelResponse\x12\x61\n\x10\x45xportUserConfig\x12%.SuperBuilder.ExportUserConfigRequest\x1a&.SuperBuilder.ExportUserConfigResponse\x12\x61\n\x10ImportUserConfig\x12%.SuperBuilder.ImportUserConfigRequest\x1a&.SuperBuilder.ImportUserConfigResponseB>Z#superbuilder/SuperBuilderWinService\xaa\x02\x16SuperBuilderWinServiceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'superbuilder_middleware_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z#superbuilder/SuperBuilderWinService\252\002\026SuperBuilderWinService'
  _globals['_SAYHELLOREQUEST']._serialized_start=47
  _globals['_SAYHELLOREQUEST']._serialized_end=78
  _globals['_SAYHELLORESPONSE']._serialized_start=80
  _globals['_SAYHELLORESPONSE']._serialized_end=115
  _globals['_CONVERSATIONHISTORY']._serialized_start=117
  _globals['_CONVERSATIONHISTORY']._serialized_end=169
  _globals['_CHATREQUEST']._serialized_start=172
  _globals['_CHATREQUEST']._serialized_end=370
  _globals['_CHATRESPONSE']._serialized_start=372
  _globals['_CHATRESPONSE']._serialized_end=403
  _globals['_STOPCHATREQUEST']._serialized_start=405
  _globals['_STOPCHATREQUEST']._serialized_end=422
  _globals['_STOPCHATRESPONSE']._serialized_start=424
  _globals['_STOPCHATRESPONSE']._serialized_end=442
  _globals['_LOADMODELSREQUEST']._serialized_start=444
  _globals['_LOADMODELSREQUEST']._serialized_end=463
  _globals['_LOADMODELSRESPONSE']._serialized_start=465
  _globals['_LOADMODELSRESPONSE']._serialized_end=501
  _globals['_CHECKHEALTHREQUEST']._serialized_start=503
  _globals['_CHECKHEALTHREQUEST']._serialized_end=544
  _globals['_CHECKHEALTHRESPONSE']._serialized_start=546
  _globals['_CHECKHEALTHRESPONSE']._serialized_end=583
  _globals['_ADDFEEDBACKREQUEST']._serialized_start=585
  _globals['_ADDFEEDBACKREQUEST']._serialized_end=695
  _globals['_ADDFEEDBACKRESPONSE']._serialized_start=697
  _globals['_ADDFEEDBACKRESPONSE']._serialized_end=735
  _globals['_ADDFILESREQUEST']._serialized_start=737
  _globals['_ADDFILESREQUEST']._serialized_end=777
  _globals['_ADDFILESRESPONSE']._serialized_start=780
  _globals['_ADDFILESRESPONSE']._serialized_end=939
  _globals['_GETFILELISTREQUEST']._serialized_start=941
  _globals['_GETFILELISTREQUEST']._serialized_end=979
  _globals['_STOPADDFILESREQUEST']._serialized_start=981
  _globals['_STOPADDFILESREQUEST']._serialized_end=1002
  _globals['_STOPADDFILESRESPONSE']._serialized_start=1004
  _globals['_STOPADDFILESRESPONSE']._serialized_end=1026
  _globals['_CLIENTDISCONNECTEDREQUEST']._serialized_start=1028
  _globals['_CLIENTDISCONNECTEDREQUEST']._serialized_end=1055
  _globals['_GETFILELISTRESPONSE']._serialized_start=1057
  _globals['_GETFILELISTRESPONSE']._serialized_end=1096
  _globals['_REMOVEFILESREQUEST']._serialized_start=1098
  _globals['_REMOVEFILESREQUEST']._serialized_end=1141
  _globals['_REMOVEFILESRESPONSE']._serialized_start=1143
  _globals['_REMOVEFILESRESPONSE']._serialized_end=1186
  _globals['_DOWNLOADFILESREQUEST']._serialized_start=1188
  _globals['_DOWNLOADFILESREQUEST']._serialized_end=1280
  _globals['_DOWNLOADFILESRESPONSE']._serialized_start=1282
  _globals['_DOWNLOADFILESRESPONSE']._serialized_end=1347
  _globals['_SETMODELSREQUEST']._serialized_start=1349
  _globals['_SETMODELSREQUEST']._serialized_end=1461
  _globals['_SETMODELSRESPONSE']._serialized_start=1463
  _globals['_SETMODELSRESPONSE']._serialized_end=1504
  _globals['_UNLOADMODELSREQUEST']._serialized_start=1506
  _globals['_UNLOADMODELSREQUEST']._serialized_end=1574
  _globals['_UNLOADMODELSRESPONSE']._serialized_start=1576
  _globals['_UNLOADMODELSRESPONSE']._serialized_end=1622
  _globals['_SETPARAMETERSREQUEST']._serialized_start=1624
  _globals['_SETPARAMETERSREQUEST']._serialized_end=1671
  _globals['_SETPARAMETERSRESPONSE']._serialized_start=1673
  _globals['_SETPARAMETERSRESPONSE']._serialized_end=1696
  _globals['_CLIENTDISCONNECTEDRESPONSE']._serialized_start=1698
  _globals['_CLIENTDISCONNECTEDRESPONSE']._serialized_end=1726
  _globals['_GETCLIENTCONFIGREQUEST']._serialized_start=1728
  _globals['_GETCLIENTCONFIGREQUEST']._serialized_end=1771
  _globals['_GETCLIENTCONFIGRESPONSE']._serialized_start=1773
  _globals['_GETCLIENTCONFIGRESPONSE']._serialized_end=1812
  _globals['_GETCHATHISTORYREQUEST']._serialized_start=1814
  _globals['_GETCHATHISTORYREQUEST']._serialized_end=1837
  _globals['_GETCHATHISTORYRESPONSE']._serialized_start=1839
  _globals['_GETCHATHISTORYRESPONSE']._serialized_end=1877
  _globals['_SETVECTORDBREQUEST']._serialized_start=1879
  _globals['_SETVECTORDBREQUEST']._serialized_end=1925
  _globals['_SETVECTORDBRESPONSE']._serialized_start=1927
  _globals['_SETVECTORDBRESPONSE']._serialized_end=1965
  _globals['_REMOVESESSIONREQUEST']._serialized_start=1967
  _globals['_REMOVESESSIONREQUEST']._serialized_end=2008
  _globals['_REMOVESESSIONRESPONSE']._serialized_start=2010
  _globals['_REMOVESESSIONRESPONSE']._serialized_end=2050
  _globals['_SETSESSIONNAMEREQUEST']._serialized_start=2052
  _globals['_SETSESSIONNAMEREQUEST']._serialized_end=2115
  _globals['_SETSESSIONNAMERESPONSE']._serialized_start=2117
  _globals['_SETSESSIONNAMERESPONSE']._serialized_end=2158
  _globals['_SETACTIVEASSISTANTREQUEST']._serialized_start=2160
  _globals['_SETACTIVEASSISTANTREQUEST']._serialized_end=2227
  _globals['_SETACTIVEASSISTANTRESPONSE']._serialized_start=2229
  _globals['_SETACTIVEASSISTANTRESPONSE']._serialized_end=2291
  _globals['_SETASSISTANTVIEWMODELREQUEST']._serialized_start=2293
  _globals['_SETASSISTANTVIEWMODELREQUEST']._serialized_end=2368
  _globals['_SETASSISTANTVIEWMODELRESPONSE']._serialized_start=2370
  _globals['_SETASSISTANTVIEWMODELRESPONSE']._serialized_end=2418
  _globals['_SETUSERCONFIGVIEWMODELREQUEST']._serialized_start=2420
  _globals['_SETUSERCONFIGVIEWMODELREQUEST']._serialized_end=2471
  _globals['_SETUSERCONFIGVIEWMODELRESPONSE']._serialized_start=2473
  _globals['_SETUSERCONFIGVIEWMODELRESPONSE']._serialized_end=2522
  _globals['_CONVERTMODELREQUEST']._serialized_start=2524
  _globals['_CONVERTMODELREQUEST']._serialized_end=2605
  _globals['_CONVERTMODELRESPONSE']._serialized_start=2607
  _globals['_CONVERTMODELRESPONSE']._serialized_end=2646
  _globals['_UPLOADMODELREQUEST']._serialized_start=2648
  _globals['_UPLOADMODELREQUEST']._serialized_end=2770
  _globals['_UPLOADMODELRESPONSE']._serialized_start=2772
  _globals['_UPLOADMODELRESPONSE']._serialized_end=2810
  _globals['_EXPORTUSERCONFIGREQUEST']._serialized_start=2812
  _globals['_EXPORTUSERCONFIGREQUEST']._serialized_end=2880
  _globals['_EXPORTUSERCONFIGRESPONSE']._serialized_start=2882
  _globals['_EXPORTUSERCONFIGRESPONSE']._serialized_end=2942
  _globals['_IMPORTUSERCONFIGREQUEST']._serialized_start=2944
  _globals['_IMPORTUSERCONFIGREQUEST']._serialized_end=2989
  _globals['_IMPORTUSERCONFIGRESPONSE']._serialized_start=2991
  _globals['_IMPORTUSERCONFIGRESPONSE']._serialized_end=3051
  _globals['_SUPERBUILDER']._serialized_start=3054
  _globals['_SUPERBUILDER']._serialized_end=5641
# @@protoc_insertion_point(module_scope)
