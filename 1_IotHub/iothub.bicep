targetScope = 'resourceGroup'

resource iotHub 'Microsoft.Devices/IotHubs@2023-06-30' = {
  name: 'fabrica'
  location: 'eastus2'
  sku: {
    name: 'S1'
    capacity: 1
  }
  properties: {
    publicNetworkAccess: 'Enabled'
    enableFileUploadNotifications: false
    features: 'None'
  }
}

output iotHubName string = iotHub.name
output iotHubResourceId string = iotHub.id
