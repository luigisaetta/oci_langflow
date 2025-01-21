# About This Repository
This repository provides the code for wrapper components that enable seamless integration 
of OCI Generative AI and OCI 23c AI Vector Store into Langflow.

## Components for Retrieval-Augmented Generation (RAG)
We include the essential components required to build a robust Retrieval-Augmented Generation (RAG) solution:

1. **OCI Embeddings Model**    
   Based on Cohere, this component generates embeddings for your data, enabling effective search and retrieval.

2. **OCI Chat Model**    
   Powered by Meta or Cohere, this component handles conversational AI tasks for natural and engaging user interactions.

3. **OCI Vector Store** 
   Built on Oracle Database 23AI, this component provides a highly efficient and scalable vector store 
   for managing and querying embeddings.

## Langflow Setup
To setup an environment with Langflow this is the recommended series of steps:

1. Create and activate a "conda environment" using Python 3.11
2. Install the tool uv in this environment, using pip
3. Install Langflow using uv. Follow the instructions [here](https://docs.langflow.org/get-started-installation)
4. Install oci Python sdk and update langchain-community

## Setup your local environment with  OCI integration
* Clone the github repository
* modify the set_env.sh file so that the LANGFLOW_COMPONENTS_PATH points to your local oci_custom directory
* execute source ./set_env.sh to set the environment variables
* start langflow using the command: uv run langflow run

## Notes
Setup: do not install Langflow directly using pip. There are many components and pip really struggle to manage them correctly.
As a result the installation is really slow. The preferred way to do (as suggested also in the official documentation) is to use
uv.

## Security
To be able to use Models in OCI Generative AI Services you must have the proper policies in place.

The code provided supports two ways to handle autorization: API_KEY and RESOURCE_PRINCIPAL.
Follows general OCI documentation to properly handle security.




