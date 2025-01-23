# About This Repository
This repository provides the code for wrapper components that enable seamless integration 
of **OCI Generative** AI and **OCI 23AI** Vector Store into Langflow.

## Components for Retrieval-Augmented Generation (RAG)
In this first release (jan 2025), we include the essential components required to build a robust Retrieval-Augmented Generation (RAG) solution:

1. **OCI Embeddings Model**    
   Based on Cohere, this component generates embeddings for your data, enabling effective search and retrieval.

2. **OCI Chat Model**    
   Powered by Meta or Cohere models, this component handles conversational AI tasks for natural and engaging user interactions.

3. **OCI Vector Store**  
   Built on Oracle Database 23AI, this component provides a highly efficient and scalable vector store 
   for managing and querying embeddings.

## Langflow Setup
To setup an environment with Langflow this is the recommended series of steps:

1. Create and activate a "conda environment" using Python 3.11
```
conda create -n oci_langflow python==3.11
conda activate oci_langflow
```
2. Install the tool [uv](https://docs.astral.sh/uv/getting-started/) in this environment, using pip
3. Install Langflow using uv. Follow the instructions [here](https://docs.langflow.org/get-started-installation)
```
uv pip install langflow
```
4. Install oci Python sdk and update langchain-community
```
pip install oci -U
```

## Setup your local environment with OCI integration
* Clone the github repository
```
git clone https://github.com/luigisaetta/oci_langflow.git
```
* modify the `set_env.sh` file. Change the env variable `LANGFLOW_COMPONENTS_PATH` to point your local **oci_custom** directory
* execute the following command to set the environment variables:
```
source ./set_env.sh
``` 
* start langflow using the command: 
```
uv run langflow run
```

## Notes
### Setup: do not install Langflow using directly pip, use uv. 
There are many components and pip really struggle to manage them correctly.
As a result the installation is really slow. 
The preferred way to do (as suggested also in the official documentation) is to use
uv.

### The **Philosophy**
The main idea is to provide the code as an easy way that can be used from customers. Then, if they want, they can add all the details they really need.
Therefore, for example, wrappers expose only the mandatory parameters that needs to be customized. For the remaining:
1. I have followed Langchain defaults.
2. The code is simple and easy to be customized.

## Security
To be able to use Models in OCI Generative AI Services you must have the proper policies in place.

The code provided supports two ways to handle authorization: 
* API_KEY (default)
* RESOURCE_PRINCIPAL.
Follow general OCI documentation to properly handle security.

## Examples
There is a simple way to start working with Langflow and our OCI integration: take one of the example flows 
and modify it plugging OCI Embeddings, OCI Chat Model and OCI Vector Store.

It is really easy and you need to choose or specify only few parameters (COMPARTMENT_OCID, ..).

Here the links to two examples with screenshots:
* [Memory Chatbot](./images/langflow-memory01.png)
* [RAG with 23AI](./images/langflow-rag01.png)




