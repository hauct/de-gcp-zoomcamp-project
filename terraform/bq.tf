resource "google_bigquery_dataset" "dev_db" {
  dataset_id = "dbt_dev"
  friendly_name = "dbt_dev"
  project    = var.project_id
  location   = var.region
  delete_contents_on_destroy = true
}

resource "google_bigquery_dataset" "prod_db" {
  dataset_id                 = "dbt_prod"
  friendly_name               = "dbt_prod"
  project                    = var.project_id
  location                   = var.region
  delete_contents_on_destroy = true
}

resource "google_bigquery_table" "tablemap-dev" {
  dataset_id          = google_bigquery_dataset.dev_db.dataset_id
  table_id            = "stg_map"
  deletion_protection = false
  external_data_configuration {
    autodetect    = false
    source_uris   = ["gs://${google_storage_bucket.bucketfred.name}/stagging/map/*"]         
    source_format = "PARQUET"   
  }
  schema = <<EOF
    [
      {
        "name": "region",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "code",
        "type": "string",
        "mode": "NULLABLE"
      },      
      {
        "name": "value",
        "type": "float",
        "mode": "NULLABLE"
      },
      {
        "name": "series_id",
        "type": "string",
        "mode": "NULLABLE"
      },      
      {
        "name": "date",
        "type": "timestamp",
        "mode": "NULLABLE"
      },      
      {
        "name": "groupid",
        "type": "integer",
        "mode": "NULLABLE"
      }
    ]
    EOF
}

resource "google_bigquery_table" "tablecategory-dev" {
  dataset_id          = google_bigquery_dataset.dev_db.dataset_id
  table_id            = "stg_category"
  deletion_protection = false
  external_data_configuration {
    autodetect    = false # true
    source_uris   = ["gs://${google_storage_bucket.bucketfred.name}/stagging/category/*"]
    source_format = "PARQUET"   
  }
  schema = <<EOF
    [
      {
        "name": "name",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "id",
        "type": "integer",
        "mode": "NULLABLE"
      },      
      {
        "name": "parent_name",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "parent_id",
        "type": "integer",
        "mode": "NULLABLE"
      }
    ]
    EOF
}


resource "google_bigquery_table" "tableseries-dev" {
  dataset_id          = google_bigquery_dataset.dev_db.dataset_id
  table_id            = "stg_series"
  deletion_protection = false
  external_data_configuration {
    autodetect    = false # true
    source_uris   = ["gs://${google_storage_bucket.bucketfred.name}/stagging/series/*"]
    source_format = "PARQUET"   
  }
  schema = <<EOF
    [
      {
        "name": "id",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "realtime_start",
        "type": "timestamp",
        "mode": "NULLABLE"
      },      
      {
        "name": "realtime_end",
        "type": "timestamp",
        "mode": "NULLABLE"
      },
      {
        "name": "title",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "observation_start",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "observation_end",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "frequency",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "frequency_short",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "units",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "units_short",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "seasonal_adjustment",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "seasonal_adjustment_short",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "last_updated",
        "type": "timestamp",
        "mode": "NULLABLE"
      },
      {
        "name": "popularity",
        "type": "integer",
        "mode": "NULLABLE"
      },
      {
        "name": "group_popularity",
        "type": "integer",
        "mode": "NULLABLE"
      },
      {
        "name": "category_id",
        "type": "integer",
        "mode": "NULLABLE"
      }
    ]
    EOF
}


resource "google_bigquery_table" "tablemap" {
  dataset_id          = google_bigquery_dataset.prod_db.dataset_id
  table_id            = "stg_map"
  deletion_protection = false
  external_data_configuration {
    autodetect    = false
    source_uris   = ["gs://${google_storage_bucket.bucketfred.name}/stagging/map/*"]         
    source_format = "PARQUET"   
  }
  schema = <<EOF
    [
      {
        "name": "region",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "code",
        "type": "string",
        "mode": "NULLABLE"
      },      
      {
        "name": "value",
        "type": "float",
        "mode": "NULLABLE"
      },
      {
        "name": "series_id",
        "type": "string",
        "mode": "NULLABLE"
      },      
      {
        "name": "date",
        "type": "timestamp",
        "mode": "NULLABLE"
      },      
      {
        "name": "groupid",
        "type": "integer",
        "mode": "NULLABLE"
      }
    ]
    EOF
}

resource "google_bigquery_table" "tablecategory" {
  dataset_id          = google_bigquery_dataset.prod_db.dataset_id
  table_id            = "stg_category"
  deletion_protection = false
  external_data_configuration {
    autodetect    = false # true
    source_uris   = ["gs://${google_storage_bucket.bucketfred.name}/stagging/category/*"]
    source_format = "PARQUET"   
  }
  schema = <<EOF
    [
      {
        "name": "name",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "id",
        "type": "integer",
        "mode": "NULLABLE"
      },      
      {
        "name": "parent_name",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "parent_id",
        "type": "integer",
        "mode": "NULLABLE"
      }
    ]
    EOF
}


resource "google_bigquery_table" "tableseries" {
  dataset_id          = google_bigquery_dataset.prod_db.dataset_id
  table_id            = "stg_series"
  deletion_protection = false
  external_data_configuration {
    autodetect    = false # true
    source_uris   = ["gs://${google_storage_bucket.bucketfred.name}/stagging/series/*"]
    source_format = "PARQUET"   
  }
  schema = <<EOF
    [
      {
        "name": "id",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "realtime_start",
        "type": "timestamp",
        "mode": "NULLABLE"
      },      
      {
        "name": "realtime_end",
        "type": "timestamp",
        "mode": "NULLABLE"
      },
      {
        "name": "title",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "observation_start",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "observation_end",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "frequency",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "frequency_short",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "units",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "units_short",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "seasonal_adjustment",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "seasonal_adjustment_short",
        "type": "string",
        "mode": "NULLABLE"
      },
      {
        "name": "last_updated",
        "type": "timestamp",
        "mode": "NULLABLE"
      },
      {
        "name": "popularity",
        "type": "integer",
        "mode": "NULLABLE"
      },
      {
        "name": "group_popularity",
        "type": "integer",
        "mode": "NULLABLE"
      },
      {
        "name": "category_id",
        "type": "integer",
        "mode": "NULLABLE"
      }
    ]
    EOF
}