import mkdocs_gen_files
from pathlib import Path


import getml
nav = mkdocs_gen_files.Nav()
src = Path(getml.__file__).parent
def get_stubs(src: Path):
    for path in sorted(src.rglob("*.py")):
        #print(path)
        module_path = path.relative_to(src).with_suffix("")
        doc_path = path.relative_to(src).with_suffix(".md")
        full_doc_path = Path("reference", doc_path)
        parts = tuple(module_path.parts)

        if parts[-1] == "__init__":
            if len(parts) == 1:
                continue
            parts = parts[:-1]
        elif parts[-1] == "__main__":
            continue

        nav[parts] = doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            fd.write(f"::: getml.{ident}")

    with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())
