
from azureml.core import Workspace, Datastore, Dataset
from azureml.core.run import Run
from azureml.core.model import Model

run = Run.get_context()
exp = run.experiment
ws = run.experiment.workspace   

dataset = Dataset.get_by_name(ws, name='data_set_folder') 

try:
    dataset.download(target_path='.', overwrite=False)
except:
    pass
  
  
# Use CTRL + / to comment out a block of code
from azureml.core import Model
from azureml.core.resource_configuration import ResourceConfiguration
#https://docs.microsoft.com/en-us/azure/machine-learning/how-to-train-tensorflow

# # upload the model file explicitly into artifacts
# Register tensorflow model
# model = run.register_model(model_name= model_name, 
#                            model_path='outputs/models',
#                            model_framework=Model.Framework.TENSORFLOW,
#                            model_framework_version='2.4.1',
#                            resource_configuration=ResourceConfiguration(cpu=1, memory_in_gb=0.5)) 

# print("Uploading the model into run artifacts...")
"""
datastore = ws.get_default_datastore() 
datastore.upload(src_dir= model_dir, target_path='target/models', overwrite=True) 
"""
# from azureml.data.datapath import DataPath 
# ds = Dataset.File.upload_directory(src_dir='./outputs/models/',
#             target=DataPath(datastore,  'target/models'),
#             show_progress=True)  
 
""" 
print("Uploaded the model {} to experiment {}".format(model_path, run.experiment.name))
dirpath = os.getcwd()
print(dirpath)
print("Following files are uploaded ")
print(run.get_file_names())  
""" 
run.complete()
