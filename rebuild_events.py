from os import getenv
from requests import get

source = getenv("SOURCE","https://raw.githubusercontent.com/github/docs/main/content/actions/using-workflows/events-that-trigger-workflows.md")

events = [ event.strip() for event in get(source).text.split("## `")][1:]
starting_blacklist = ("|", "**Note**","**Note:**", "{%")
completion_lines_arr = ""
for event in events:
    description=[event_info for event_info in event.split("\n") if not event_info.startswith(starting_blacklist) and event_info != ""][1].replace("{% data variables.product.product_name %}", "GitHub").split(".")[0].replace("'"," ")
    name=event.split("\n")[0].split("`")[0]
    completion_lines_arr+=f"\t\t'{name}:{description}'\n"
    print(f"'{name}:{description}'")

r = open("_act", "r").read()
original = r.split("# --- gen ---")[1]
new = f"\n{completion_lines_arr}"
open("_act", "w").write(r.replace(original, new))