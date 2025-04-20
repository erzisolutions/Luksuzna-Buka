from pathlib import Path
def run(input_path: Path, out_dir: Path, *args, **kwargs):
    # TODO: implement workflow_restore
    out_dir.mkdir(exist_ok=True)
    (out_dir/"workflow_restore.py_NOT_IMPLEMENTED.txt").write_text("Workflow placeholder")
