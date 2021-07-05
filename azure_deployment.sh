#!/bin/bash

az group create \
  --location $RG_LOCATION \
  --name $RG_NAME

az postgres up \
  --resource-group $RG_NAME \
  --location $RG_LOCATION \
  --sku-name $SKU_NAME \
  --server-name $SERVER_NAME \
  --database-name $DB_NAME \
  --admin-user $DB_USER_NAME \
  --admin-password $DB_PASS \
  --ssl-enforcement Enabled

az webapp up \
  --resource-group $RG_NAME \
  --location  $RG_LOCATION \
  --plan $PLAN_NAME \
  --sku $SKU \
  --name $WEBAPP_NAME

az webapp config appsettings set \
  --settings \
    DBHOST=$SERVER_NAME \
    DBNAME=$DB_NAME \
    DBUSER=$DB_USER_NAME \
    DBPASS=$DB_PASS \
  --resource-group $RG_NAME