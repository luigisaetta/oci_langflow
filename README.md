# OCI Langflow
This repository contains the code for the wrapper components enabling to
integrate OCI Generative AI and OCI 23AI Vector Store in Langflow

We provide the code for the 3 basic components needed to develop a
Retrieval Augmented Generation (RAG) solution:
* OCI Embeddings Model (based on Cohere)
* OCI Chat Model (Meta or Cohere)
* OCI Vector Store (based on 23AI)

## Langflow Setup
To setup an environment with Langflow this is the recommended series of steps:

1. Create and activate a "conda environment" suing Python 3.11
2. Install the tool uv in this environment, using pip
3. Install Langflow using uv (follow the instructions [here](https://docs.langflow.org/get-started-installation)
4. Install oci Python sdk and update langchain-community

## Setup your local environment with  OCI integration
* Clone the github repository
* modify the set_env.sh file somthat the LANGFLOW_COMPONENTS_PATH points to your local oci_custom directory
* execute source ./set_env.sh to set the environment variables
* start langflow using uv run langflow run


