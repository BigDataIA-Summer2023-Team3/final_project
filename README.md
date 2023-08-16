# STACKAI 🤖👨‍💻

## Please find the app hosted on GCP (for a limited time only) - 

User Interface : [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](http://34.102.9.117:30005/)

Backend : [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)](http://34.102.9.117:30004/docs)

Data Pipeline : [![Apache Airflow](https://img.shields.io/badge/Apache_Airflow-007A88?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)](http://34.102.9.117:8080/)

Documentation : [![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1QLTgE_6TTnMbBc1Sw0KOtDvdpv3VR2oRGZPVJhNTFgs#0)

App Demo : [![Youtube](https://img.shields.io/badge/Youtube-808080?style=for-the-badge&logo=YouTube&logoColor=white)](https://youtu.be/DnmAYNL0kcI)



## Introduction :memo: 

In response to a noticeable decline in traffic on Stack Overflow – once a thriving developer community platform – due to the rise of OpenAI's ChatGPT, an application named "StackAI" has been developed. 

This strategic endeavor aims to restore Stack Overflow's status as a preferred destination for developers seeking coding solutions. By integrating advanced AI features, StackAI strives to rejuvenate community engagement while preserving its core values.

At the core of StackAI lies the Category-Question-Answer paradigm. Users select a category of their choice, enabling focused exploration. Upon posing a question, StackAI employs cutting-edge AI models to generate precise answers in real-time. To enhance credibility, the platform intelligently curates and presents the three most relevant questions from Stack Overflow's vast repository, along with essential statistics such as accepted answers, comments, scores, owner's reputation and so on.

In cases where no accepted answer exists, StackAI generates a reliable response. For lengthy accepted answers, the platform provides concise summaries, fostering efficient comprehension. Our commitment to user satisfaction is unwavering — if the user's question still remain unanswered, StackAI facilitates easy transition to Stack Overflow's human-driven ecosystem. The platform crafts well-structured questions in Stack Overflow format, easing the process of posting a question to seek human assistance.

Advanced AI models such as OpenAI and Sentence Transformer were fine tuned to provide high-quality custom responses. A robust Airflow data pipeline, powered by meticulous data collection, pre-processing and validation, forms the backbone. FASTAPI ensures a responsive backend, while Streamlit creates an intuitive user interface. Terraform seamlessly provisions vital GCP resources such as BigQuery, CloudSQL and Compute Engine.

Ultimately, StackAI aims to create a better environment where human knowledge and AI work together to boost innovation and growth.


## Project Goals :dart:

The goal of StackAI is to rejuvenate community engagement on Stack Overflow by integrating advanced AI features. The platform presents relevant questions from Stack Overflow’s repository and generates reliable responses backed by human answers. StackAI aims to create an environment where human knowledge and AI work together to boost innovation and growth.


## Data Source 📚:

The data for this project is sourced from Google Bigquery public Stackoverflow Dataset, which consists of over 10 tables, with several million rows of data - [StackOverflow dataset](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sstackoverflow&project=firstproject-390804) 

## Process Outline

**2. Data Preprocessing:** Out of the 15 tables within the Stack Overflow public dataset, a deliberate selection was made by opting for 6 pertinent tables such as badges, comments, posts_questions, etc., aligning with the project's specific needs. Following this selection, a comprehensive exploratory data analysis was conducted, leading to the transformation of these chosen tables into two optimized entities: Posts and Comments. This transformation process involved the careful elimination of extraneous columns and the mitigation of null values, thereby enhancing the data quality.

**3. Data Pipeline:** In this project, a robust data pipeline is established to Extract, Transform, Load (ETL) operations through Airflow. This pipeline orchestrates the extraction of raw data, its transformation to conform to the desired structure, and the loading of cleaned and enriched data into target destinations. The pipeline also automates the creation and storage of embeddings along with performing Great Expectations analysis.

**5. Data Validation:** Used Great Expectations to validate the gathered data, confirming its conformity to anticipated formats and values.

**4. Model Selection:** Models like SentenceTransformer -'distilbert-base-nli-stsb-mean-tokens' and openAI's 'gpt-3.5-turbo' and 'text-davinci-003' were selected and fine tuned based on the features implemented on StackAI.

### Features :

- **Retrieve related questions from Stack Overflow:** distilbert-base-nli-stsb-mean-tokens’ model from SentenceTransformer: This model was chosen for its ability to convert text sentences into meaningful embeddings, capturing semantic context and similarity relationships. Its design, optimized for sentence similarity tasks, aligns perfectly with the project’s goal of determining question relevance by effectively analyzing the textual content of user inputs and matching them with relevant questions in Stack Overflow’s repository. The model performs cosine similarity comparison to determine the most relevant questions.

- **Accepted answer Summarization:** ‘text-davinci-003’ model from OpenAI: This model was chosen for its ability to provide concise summaries of lengthy accepted answers. The model was fine-tuned to generate coherent and contextually relevant summaries, fostering efficient comprehension. The fine-tuning process involved providing custom prompts and adjusting the model’s temperature to improve its performance on summarizing programming-related answers.

- **StackAI Generated Answers:** ‘gpt-3.5-turbo’ model from OpenAI: This functionality leverages an OpenAI - GPT 3.5 Turbo model tailored for generating custom responses. The model was chosen for its advanced language generation capabilities, enabling the creation of coherent and contextually relevant answers. The model was fine-tuned by providing custom prompts and adjusting its temperature to improve its performance on generating answers for StackAI's features namely - 'Ask a question', 'Generate an answer if accepted answer doesn’t exist' and 'Craft a question', thereby enriching the overall user experience and ensuring they receive comprehensive and precise information.

**6. Backend:** FASTAPI serves as a vital component, orchestrating seamless communication between AI models and Streamlit, and enabling efficient user authentication. It ensures a robust connection between various modules, allowing smooth data exchange and interactions between the AI models and the user interface, making it easy to interact with the AI-generated responses and enhancing the overall application's usability.

**7. User Interface:** A Streamlit based app that offers an instinctive interface enabling users to effortlessly to register, ask any programming question, get StackAI responses, view related questions from Stack Overflow, view essential Stack Overflow details for these questions, get summaries for the accepted answer and even an option to ask StackAI to craft a question to post on Stack Overflow.

**8. Infrastructure as a Service (IaaS):** Terraform was utilized to establish essential GCP resources including CloudSQL, BigQuery, and compute instance. These resources are seamlessly integrated within the application, enabling automated functionality and streamlining its operational efficiency.

**9. Deployment:** Deployed a dockerized app on GCP

**10. Continuous Integration:** Employed GitHub Actions to perform unit testing with Pytest on any latest code that is pushed into the repo, assuring the effectiveness of the application and its integral components.

## Project Architecture Diagram

![Implemented Architecture Diagram](https://github.com/Sukruthmothakapally/DAMG7245-Summer2023/raw/Sukruth-branch/final_project/Implemented_architecture_diagram.jpg)



## TO run the dockerized App locally -

1. To clone this repository, use the following command:

```bash
git clone https://github.com/Sukruthmothakapally/DAMG7245-Summer2023.git
```

2. Navigate to streamlit/pages/ and replace ``fastapi:8095`` with ``localhost:8000`` in all the ``.py`` files
3. [Install Docker](https://docs.docker.com/engine/install/ubuntu/)
4. [Install Terraform](https://developer.hashicorp.com/terraform/downloads)
5. [Install Google cloud SDK](https://cloud.google.com/sdk/gcloud)
6. [Create a GCP account](https://cloud.google.com/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1605212&utm_content=text-ad-none-any-DEV_c-CRE_665665924744-ADGP_Hybrid+%7C+BKWS+-+MIX+%7C+Txt_General+GCP-KWID_43700077224933058-kwd-353549070178&utm_term=KW_gcp+console-ST_gcp+console&gclid=CjwKCAjwxOymBhAFEiwAnodBLKy1QR6zNZI8WfmBryMskXcRVImg9pDr5MV_RXhns8DLPdl_gwQ0khoCoU0QAvD_BwE&gclsrc=aw.ds&hl=en)
7. Create a service account with the permissions for accessing BigQuery, CloudSQL, and Cloud Instances.
8. Download the service account's key in json format
9. Run these commands to connect your system to your GCP account -
```bash
Set google_application_credentials=path_to_json_file
gcloud auth application-default set-quota-project your_project_id_here
```
9. Create a .env file in the root directory with the following variables:
```bash
AIRFLOW_UID= 'user id of your machine'

AIRFLOW_PROJ_DIR= 'The dir where airflow is present'

DB_HOST= 'CloudSQL instance public IP'

DB_USER= 'CloudSQL database username'

DB_PASSWORD= 'CloudSQL database password'

DB_NAME= 'CloudSQL database name'

DB_PORT= 'CloudSQL database port number'

OPENAI_API_KEY= 'Your OpenAI API key for accessing the GPT model.'
```
10. Navigate to Terraform dir and comment out the resource - ``google_compute_instance`` if you don't want the app hosted on GCP
11. Navigate to ``Terraform/`` path to create the GCP infrastructure with Terraform
12. Run the following commands -
```bash
terraform init
terraform plan
terraform apply --auto-approve
```
14. Once you have set up your environment variables, start Airflow by running the following command from the root directory:
```bash
docker compose up
```
11. Access the Airflow UI by navigating to ``http://localhost:8080/`` in your web browser.
12. To run the DAGs in Airflow, click on the dags links on the Airflow UI and toggle the switch to enable the DAGs.
13. (Optional) - You can trigger a dag with custom input by selecting ``Trigger dag w/ config``
14. Once the DAGs have run successfully, access the Streamlit application by navigating to ``http://localhost:8090/``
15. First sign up and then sign in to use the StackAI app and explore it's features


## To stop the app -
17. Run this command inside terraform/ to destroy the GCP infrastructure created by terraform -
```bash
terraform destroy --auto-approve
```
17. Run this command in project home dir to stop docker -
```bash
docker compose down
```

