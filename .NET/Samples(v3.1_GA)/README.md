# Azure AI Document Intelligence Code Samples

> [!NOTE]
> Form Recognizer is now **Azure AI Document Intelligence**!




Code samples for each language's SDK are in the links below. Click to choose one（default **Python**）.
|Python| [.NET](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence)|[Java](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/documentintelligence/azure-ai-documentintelligence)| [JavaScript](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest)|
| --- | --- | --- | --- |


>- The contents of this guide applies to the samples of vXXX(GA),  versions: [vXXX (GA)](), [vXXX (GA)]().

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the samples](#running-the-samples)
  - [Common samples](#common-samples)
  - [Retrieval Augmented Generation (RAG) samples](#retrieval-augmented-generation-rag-samples)
  - [Pre/post processing samples](#prepost-processing-samples)
- [Next steps](#next-steps)




## Features
Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/?view=doc-intel-4.0.0) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.

## Prerequisites
* Python XXX or later is required to use this package
* You must have an [Azure subscription][azure_subscription]  and an [Azure Document Intelligence account][azure_document_intelligence_account] to run these samples.
* All of these samples need the endpoint to your Document Intelligence resource ([instructions on how to get endpoint][get-endpoint-instructions]), and your Document Intelligence API key ([instructions on how to get key][get-key-instructions]).

## Setup

1. Install the Azure Document Intelligence client library for Python with [pip][pip]:

```bash
pip install XXX
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Running the samples

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. If necessary, click [Example Document](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/tree/master/curl/form-recognizer) to get your document URL.
4. Below are some sample code guidelines so that you can choose the sample according to your needs.

### Common samples
|Topic model  |       Desription      | 
| --- | --- |
|[Read](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_read.py)   |Extract printed and handwritten text. Such as  "Extract texts from a document".|  
|[Layout](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_layout.py)   |Extract text, tables, selection marks and document structure. Such as "Analyze the document structure"，"Extract key-value pairs from a document".|
|[Prebuilt](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_tax_us_w2.py)   |Extract data from an invoice/receipt/ID/... document.|
|[Add-on capabilities](~)   |Extract font property,formula,high resolution,barcode and key value pairs, detact language and query fields.|
|[Custom model](~)   |Train a custom model and extract data from it. |

> Click to view earlier versions: [v3.2(GA)](), [v3.1 (GA)](), [v3.0 (GA)]().


### Pre/post processing samples


There are usually some pre/post processing steps that are needed to get the best results from the Document Intelligence models. These steps are not part of the Document Intelligence service, but are common steps that are needed to get the best results. The following samples show how to do these steps.

| File Name | Description |
| --- | --- |
| [sample_disambiguate_similar_characters.ipynb](Python/sample_disambiguate_similar_characters.ipynb) and [sample_disambiguate_similar_characters.py](Python/sample_disambiguate_similar_characters.py) | Sample postprocessing script to disambiguate similar characters based on business rules. |
| [sample_identify_cross_page_tables.ipynb](Python/sample_identify_cross_page_tables.ipynb) and [sample_identify_cross_page_tables.py](Python/sample_identify_cross_page_tables.py) | Sample postprocessing script to identify cross-page tables based on business rules. |
> Applies to all versions.




## Next steps

Check out the [API reference documentation][python-di-ref-docs] to learn more about
what you can do with the Azure Document Intelligence client library.


[azure_identity]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity

[pip]: https://pypi.org/project/pip/
[azure_subscription]: https://azure.microsoft.com/free/
[azure_document_intelligence_account]: https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account?tabs=singleservice%2Cwindows
[azure_identity_pip]: https://pypi.org/project/azure-identity/
[python-di-ref-docs]: https://aka.ms/azsdk/python/documentintelligence/docs
[get-endpoint-instructions]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md#get-the-endpoint
[get-key-instructions]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md#get-the-api-key
[changelog]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/CHANGELOG.md


[sample_path]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples