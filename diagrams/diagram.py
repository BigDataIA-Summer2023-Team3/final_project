from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.container import Docker
from diagrams.onprem.iac import Terraform
from diagrams.gcp.compute import ComputeEngine, GCE 
from diagrams.programming.framework import Fastapi, FastAPI
from diagrams.saas.analytics import Snowflake
from diagrams.programming.language import Python
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.compute import Server

with Diagram("Proposed Architecture for STACKAI", show=True):

    streamlit = Custom("Streamlit", "./logos/streamlit.jpg")
    docker = Docker("Docker")
    #github actions
    github = Custom("Github Actions", "./logos/githubactions.jpg")
    terraform = Terraform("Terraform")
    gcp = GCE("Google Cloud Platform") 
    fastapi = FastAPI("FAST API Backend")
    snowflake = Snowflake("Snowflake")

    airflow = Airflow("Airflow DAGs")
    

    with Cluster("Airflow"):
        extract = Custom("Extract data", "./logos/stackoverflow.jpg")
        convert = Custom("Convert data", "./logos/xmltocsv.jpg")
        clean = Custom("Transform Data", "./logos/datatransform.jpg")
        load = Custom("load data into snowflake", "./logos/dataset.jpg")
        embeddings = Custom("Store embeddings", "./logos/openai.jpg")

        airflow >> extract >> convert >> clean >> load >> embeddings

    with Cluster("Streamlit"):
        signup = Custom("user sign up", "./logos/usersignup.jpg")
        signin = Custom("logged-in user", "./logos/user.jpg")
        category = Custom("Select category and tags", "./logos/userselection.jpg")
        #user input
        user_input = Custom("User input", "./logos/userinput.jpg")

        with Cluster("OpenAI"):
            openai_logo = Custom("", "./logos/openai.jpg")
            similar_topics = Server("similarity search")
            summary_display = Server("OpenAI summary")
            langchain_answer = Server("Langchain generative QA")

            openai_logo >> similar_topics >> summary_display >> langchain_answer

        streamlit >> signup >> signin >> category >> user_input >> openai_logo

    

    with Cluster("Streamlit Other Features"):
        stats = Custom("Stackoverflow stats", "./logos/stackoverflow.jpg")
        expectations = Custom("Great Expectations", "./logos/greatexpectations.jpg")
        dashboard = Custom("User Dashboard", "./logos/userdashboard.jpg")

        streamlit >> stats >> expectations >> dashboard



    with Cluster("Docker"):
        dockerize_airflow = Airflow("Airflow")
        dockerize_fastapi = FastAPI("FastAPI")
        dockerize_streamlit = Custom("Streamlit", "./logos/streamlit.jpg")

        docker >> dockerize_airflow >> dockerize_fastapi >> dockerize_streamlit

    streamlit<<Edge(label="Dockerise the whole app")<<docker>>terraform>>Edge(label="Deploy app on GCP")>>gcp

    with Cluster("Github Actions"):
        push_project = Custom("Pytest", "./logos/pytest.jpg")
        pytest_unit_test = Custom("Pylint", "./logos/pylint.jpg")

        github >> push_project >> pytest_unit_test

    gcp << Edge(label="Continuous Integration and Deployment") >> github

    streamlit<<Edge(label="Used to make API calls")>>fastapi
    fastapi<<Edge(label="Connect with credentials")>>snowflake<<Edge(label="Perform Extract, Transform & Load")<<airflow
