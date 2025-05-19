# Special Query Types

Special queries are used to `focus` the assistant on specific documents. This can yield better, more accurate results and help the assistant answer more sophisticated questions based on the context of the specified document(s). To use the special queries click the attach file icon (the paperclip icon next to the question entry field).



**PRO TIP:** Using small files which only contain information relevant to the topic at hand will yield the best results.

To close `Special query mode` click the `Clear` icon from the list of special queries. Starting a new chat session will also exit special query mode.

![image](https://github.com/user-attachments/assets/87fa56d3-8abe-476d-97ac-62e030b1a6c7)


### Query Tabular Data
This feature is meant for analysing and querying tabular files (XLSX, CSV). 

**NOTE:** Before using this feature, ensure that the data is structured as a relational SQL table. The first row should contain the column headers, with each following row representing corresponding data entries. Avoid duplicate column names within any worksheet. For XLSX files with multiple worksheets, each worksheet will be treated as a separate table.

![image](https://github.com/user-attachments/assets/0d7d92e9-4bb6-445e-85a5-336aeabd0a6d)


### Resume Match
This feature provides HR professionals with a powerful tool to quickly identify the most qualified candidates from large applicant pools, while maintaining the ability to dive deeper into specific candidate qualifications through natural conversation. It intelligently scores resumes against job descriptions, extracts key details from top candidates using RAG, and facilitates continuous conversational analysis of resume documents. The system is designed to deliver all relevant information in a streamlined, concise, and efficient way.

**Note:** It utilizes an in-house proprietary document scoring algorithm capable of leveraging an LLM to evaluate an unlimited number of documents against specific criteria. This algorithm is customizable and can be applied to a wide range of document scoring use cases. For optimal results, use the Qwen2.5 or Qwen2 models.

![image](https://github.com/user-attachments/assets/5b83c4dc-8f02-4a7a-90c7-c8be4b673bee)

