import httplib2
from apiclient import discovery


def get_service(credentials):
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    return service


def get_nbahub_folder(service, folder_name):
    response = service.files().list(q="mimeType='application/vnd.google-apps.folder' and name='{folder_name}'".format(folder_name=folder_name),
                                    fields="files(id, name)").execute()
    folder = response.get("files")
    if not folder:
        print(f"Folder {folder_name} does not exist. Creating it.")
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = service.files().create(body=folder_metadata,
                                        fields='id').execute()
        print("Created folder. ID: {id}".format(id=folder.get('id')))
        folder = [folder]
    folder_id = folder[0]['id']
    return folder_id


def update(service, files):
    pass
