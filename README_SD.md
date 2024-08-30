# DIN-SQL Evaluation for SQLDRILLER
This README is used to guide the evaluation of SQLDriller.

## Prerequisites
Follow the same instructions in the `setup` section of README.md to create a running environment.

## Reproduce on Spider
Inference with the **original** train dataset:
```sh
python DIN-SQL_original_prompt.py --schema_path data/spider/metadata_opt/tables.json --dev_path data/spider/metadata_opt/gold_checked/dev.json
```

Inference with the **refined** train dataset:
```sh
python DIN-SQL_refined_prompt.py --schema_path data/spider/metadata_opt/tables.json --dev_path data/spider/metadata_opt/gold_checked/dev.json
```

Inference with the **refined** train dataset to generate multiple predictions:
```sh
python DIN-SQL_refined_prompt_multiple_preds.py --schema_path data/spider/metadata_opt/tables.json --dev_path data/spider/metadata_opt/gold_checked/dev.json
```
