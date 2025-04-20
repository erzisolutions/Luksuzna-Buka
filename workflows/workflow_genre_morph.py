from pathlib import Path
def run(input_path: Path, out_dir: Path, *args, **kwargs):
    # TODO: implement workflow_genre_morph
    out_dir.mkdir(exist_ok=True)
    (out_dir/"workflow_genre_morph.py_NOT_IMPLEMENTED.txt").write_text("Workflow placeholder")
