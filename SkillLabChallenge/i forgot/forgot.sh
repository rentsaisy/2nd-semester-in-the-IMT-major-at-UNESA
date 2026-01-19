export REGION=""
export PROJECT_ID=$(gcloud config get-value project)
export PROJECT_NUMBER=$(gcloud projects describe "$PROJECT_ID" --format="json" | jq -r '.projectNumber')

# Set resource names (based on actual lab values)
export BUCKET_NAME=""
export SPEECH_BUCKET="${BUCKET_NAME}-speech"
export NL_BUCKET="${BUCKET_NAME}-nl"
export DATASET_NAME=""
export TABLE_NAME=""
export CLUSTER_NAME="dataproc-cluster-$(date +%s)"

# Output file names and paths
export SPEECH_OUTPUT=""
export NL_OUTPUT=""

# Enable all required APIs
gcloud services enable dataflow.googleapis.com
gcloud services enable dataproc.googleapis.com
gcloud services enable speech.googleapis.com
gcloud services enable language.googleapis.com
gcloud services enable bigquery.googleapis.com
gcloud services enable storage.googleapis.com
gcloud services enable apikeys.googleapis.com
