#google cloud provider
provider "google" {
  credentials = file("C:\\Users\\Dell\\OneDrive - Northeastern University\\courses\\big data and intl analytics\\DAMG7245-Summer2023\\final_project\\airflow\\dags\\servicekey.json")
  project     = "stackai-394819"
  region      = "us-west2"
}
#bigquery dataset
resource "google_bigquery_dataset" "stackai" {
  dataset_id = "StackAI"
  location = "US"
}
#bigquery tables
resource "google_bigquery_table" "posts_cleaned" {
  dataset_id = google_bigquery_dataset.stackai.dataset_id
  table_id   = "posts_cleaned"

  schema = jsonencode([
    {
      name = "question_id",
      type = "INTEGER"
    },
    {
      name = "question_title",
      type = "STRING"
    },
    {
      name = "question_body",
      type = "STRING"
    },
    {
      name = "question_tags",
      type = "STRING"
    },
    {
      name = "question_score",
      type = "INTEGER"
    },
    {
      name = "question_view_count",
      type = "INTEGER"
    },
    {
      name = "answer_count",
      type = "INTEGER"
    },
    {
      name = "comment_count",
      type = "INTEGER"
    },
    {
      name = "question_creation_date",
      type = "STRING"
    },
    {
      name = "accepted_answer",
      type = "STRING"
    },
    {
      name = "accepted_answer_creation_date",
      type = "STRING"
    },
    {
      name = "accepted_answer_owner_display_name",
      type = "STRING"
    },
    {
      name = "owner_reputation",
      type = "INTEGER"
    },
    {
      name = "owner_badge",
      type = "STRING"
    },
    {
      name = "accepted_answer_score",
      type = "INTEGER"
    },
    {
      name = "accepted_answer_view_count",
      type = "INTEGER"
    }
  ])
  deletion_protection = false
}

resource "google_bigquery_table" "comments_cleaned" {
  dataset_id = google_bigquery_dataset.stackai.dataset_id
  table_id   = "comments_cleaned"

  schema = jsonencode([
    {
      name = "post_id",
      type = "INTEGER"
    },
    {
      name = "text",
      type = "STRING"
    },
    {
      name = "creation_date",
      type = "STRING"
    },
    {
      name = "score",
      type = "INTEGER"
    }
  ])
  deletion_protection = false
}

#cloud sql instance
resource "google_sql_database_instance" "postgres_instance" {
  name             = "stackai-dbinstance"
  database_version = "POSTGRES_15"
  region           = "us-west2"
  deletion_protection = false

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled    = true

    authorized_networks {
        name  = "local-dev"
        value = "0.0.0.0/0"
      }
    }
  }
}

#cloud sql database
resource "google_sql_database" "postgres_db" {
  name     = "stackai"
  instance = google_sql_database_instance.postgres_instance.name
}

#cloud sql user
resource "google_sql_user" "postgres_user" {
  name     = "stackai"
  instance = google_sql_database_instance.postgres_instance.name
  password = "hello123"
}
#cloud sql firewall
output "instance_address" {
  value = google_sql_database_instance.postgres_instance.public_ip_address
}

#gcp compute instance
resource "google_compute_instance" "default" {
  name         = "stackai-instance"
  machine_type = "e2-standard-4"
  zone         = "us-west2-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 60
      type  = "pd-balanced"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  service_account {
    email = "stackaiuser@stackai-394819.iam.gserviceaccount.com"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }

  #  metadata = {
  #   startup-script = <<-EOT
  #     #!/bin/bash
  #     exec > >(tee -i /var/log/myscript.log)
  #     exec 2>&1
  #     set -eux

  #     # Remove unwanted packages
  #     for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do 
  #       sudo apt-get remove -y $pkg; 
  #     done

  #     # Install required packages
  #     sudo apt-get update
  #     sudo apt-get install -y ca-certificates curl gnupg software-properties-common

  #     # Set up Docker repository
  #     sudo install -m 0755 -d /etc/apt/keyrings
  #     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  #     sudo chmod a+r /etc/apt/keyrings/docker.gpg
  #     echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  #     sudo apt-get update
  #     sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose

  #     # Allow necessary ports
  #     sudo ufw allow 30004/tcp
  #     sudo ufw allow 30005/tcp
  #     sudo ufw allow 8080/tcp

  #     # Create application directory and set ownership
  #     sudo mkdir /app
  #     sudo chown $(whoami):$(whoami) /app

  #     # Clone your app from a GitHub repository
  #     cd /app
  #     git clone --branch Sukruth-branch https://github.com/Sukruthmothakapally/DAMG7245-Summer2023.git
  #     cd DAMG7245-Summer2023/final_project
  #     # Create .env file with specified environment variables
  #     cat > .env <<EOF
  #     AIRFLOW_UID=1000=2
  #     AIRFLOW_PROJ_DIR=./airflow 
  #     EOF
  #     # Set the DB_HOST environment variable using the value of the instance_address output from Terraform
  #     export DB_HOST=${google_sql_database_instance.postgres_instance.public_ip_address}
  #     sudo docker compose up -d
  #   EOT
  # }

  tags = ["http-server", "https-server"]
}
