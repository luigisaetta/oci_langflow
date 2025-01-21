# OCI Langflow
This repository contains the code for the wrapper components enabling to
**integrate OCI Generative AI and OCI 23AI Vector Store in Langflow**

We provide the code for the 3 basic components needed to develop a
Retrieval Augmented Generation (RAG) solution:
* **OCI Embeddings Model** (based on Cohere)
* **OCI Chat Model** (Meta or Cohere)
* **OCI Vector Store** (based on 23AI)

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




