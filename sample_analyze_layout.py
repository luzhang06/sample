# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_layout.py

DESCRIPTION:
    This sample demonstrates how to extract text, tables, selection marks, and layout information from a document
    given through a file.
    
    Note that selection marks returned from begin_analyze_document(model_id="prebuilt-layout") do not return the text
    associated with the checkbox. For the API to return this information, build a custom model to analyze the
    checkbox and its text. See sample_build_model.py for more information.

PREREQUISITES:
    Necessary prerequisites are listed below.
    To find more details,please click the following "How-to guides" link to visit the Documentation.
    (https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api?view=doc-intel-4.0.0&tabs=windows&pivots=programming-language-python) 

    -------Python and IDE------
    1) Python3.7 or latter (https://www.python.org/) .Your Python installation should include pip (https://pip.pypa.io/en/stable/).
    2) The latest version of Visual Studio Code (https://code.visualstudio.com/) or your preferred IDE. 
    
    ------Azure AI services or Document Intelligence resource------ 
    Create a single-service (https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer)
    or multi-service (https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesAllInOne).
    You can use the free pricing tier (F0) to try the service，and upgrade later to a paid tier for production.
    
    ------Get the key and endpoint------
    1) After your resource deploys, select "Go to resource". 
    2) In the left navigation menu, select "Keys and Endpoint". 
    3) Copy one of the keys and the Endpoint for use in this sample. 
    
    ------Set your environment variables------
    1) At a command prompt, run the following commands (for Windows)，and replace <yourKey> and <yourEndpoint> with the values from your resource in the Azure portal:
       setx DOCUMENTINTELLIGENCE_API_KEY <yourKey>
       setx DOCUMENTINTELLIGENCE_ENDPOINT <yourEndpoint>
    2) Restart any running programs that read the environment variable.
    If your system is macOS or Linux，please visit the "How-to guides" link at the top to find the detailed method.

    ------Set up your programming environment------
    At a command prompt，run the following code to install the Azure AI Document Intelligence client library for Python with pip:
    pip install azure-ai-documentintelligence==1.0.0b1
    
    ------Create your Python application------
    1) Create a new Python file called sample_analyze_layout.py in an editor or IDE.
    2) Open the sample_analyze_layout.py file,copy and paste this code sample into your application.
    3) At a command prompt, use the following code to run the Python code： 
       python sample_analyze_layout.py
"""

import os


def get_words(page, line):
    result = []
    for word in page.words:
        if _in_span(word, line.spans):
            result.append(word)
    return result


def _in_span(word, spans):
    for span in spans:
        if word.span.offset >= span.offset and (word.span.offset + word.span.length) <= (span.offset + span.length):
            return True
    return False


def analyze_layout():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.documentintelligence import DocumentIntelligenceClient
    from azure.ai.documentintelligence.models import AnalyzeResult
    
    # For how to obtain the endpoint and key, please see PREREQUISITES above.
    endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
    key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]

    document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    
    # Analyze a local document：
    # Enter the actual file path in the following "path_to_sample_documents" variable.
    path_to_sample_documents = os.path.abspath(
        os.path.join(
            os.path.abspath(__file__),
            "..",
            ".<YOUR_FILE_NAME>", # Replace with your actual file name.
        )
    )
    with open(path_to_sample_documents, "rb") as f:
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-layout", analyze_request=f, content_type="application/octet-stream"
        )
        
    # Analyze a document at a URL：
    # Delete or comment out the part of "Analyze a local document" above.
    # Uncomment the following 5 lines of code. 
    # formUrl = "<YOUR_ACTUAL_fORMURL>" # Replace with the actual formUrl.
    # with open(formUrl, "rb") as f:
    #     poller = document_intelligence_client.begin_analyze_document(
    #         "prebuilt-layout", analyze_request=f, content_type="application/octet-stream"
    #     )        
    result: AnalyzeResult = poller.result()
    # To find more URLs of sample documents,visit the "How-to guides" link at the top. 

    # [START extract_layout]
    # Analyze whether document contains handwritten content.
    if result.styles and any([style.is_handwritten for style in result.styles]):
        print("Document contains handwritten content")
    else:
        print("Document does not contain handwritten content")

    # Analyze pages.
    for page in result.pages:
        print(f"----Analyzing layout from page #{page.page_number}----")
        print(f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}")

        # Analyze lines.
        if page.lines:
            for line_idx, line in enumerate(page.lines):
                words = get_words(page, line)
                print(
                    f"...Line # {line_idx} has word count {len(words)} and text '{line.content}' "
                    f"within bounding polygon '{line.polygon}'"
                )

                # Analyze words.
                for word in words:
                    print(f"......Word '{word.content}' has a confidence of {word.confidence}")

        # Analyze selection marks.
        if page.selection_marks:
            for selection_mark in page.selection_marks:
                print(
                    f"Selection mark is '{selection_mark.state}' within bounding polygon "
                    f"'{selection_mark.polygon}' and has a confidence of {selection_mark.confidence}"
                )

    # Analyze tables.
    if result.tables:
        for table_idx, table in enumerate(result.tables):
            print(f"Table # {table_idx} has {table.row_count} rows and " f"{table.column_count} columns")
            if table.bounding_regions:
                for region in table.bounding_regions:
                    print(f"Table # {table_idx} location on page: {region.page_number} is {region.polygon}")
            # Analyze cells.
            for cell in table.cells:
                print(f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'")
                if cell.bounding_regions:
                    for region in cell.bounding_regions:
                        print(f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'")

    print("----------------------------------------")
    # [END extract_layout]


if __name__ == "__main__":
    from azure.core.exceptions import HttpResponseError
    from dotenv import find_dotenv, load_dotenv

    try:
        load_dotenv(find_dotenv())
        analyze_layout()
    except HttpResponseError as error:
        # Examples of how to check an HttpResponseError
        # Check by error code:
        if error.error is not None:
            if error.error.code == "InvalidImage":
                print(f"Received an invalid image error: {error.error}")
            if error.error.code == "InvalidRequest":
                print(f"Received an invalid request error: {error.error}")
            # Raise the error again after printing it
            raise
        # If the inner error is None and then it is possible to check the message to get more information:
        if "Invalid request".casefold() in error.message.casefold():
            print(f"Uh-oh! Seems there was an invalid request: {error}")
        # Raise the error again
        raise
