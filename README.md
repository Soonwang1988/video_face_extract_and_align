# deepfacelab_data_extract_only


###### create environment
```
conda env create -f deepfacelab.yml
```


#### after creating env we have to add enivornment variables
```commandline
conda deactivate
conda activate deepfacelab
```


###### extract and align face
```
python data_extract.py /path/to/parent_data
```

Replace /path/to/parent_data with the path to the parent data directory containing the video files


