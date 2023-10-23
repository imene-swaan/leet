from typing import List
import xml.etree.ElementTree as ET
from pathlib import Path



def split_xml(path:str, output_dir:str, max_children:int = 1000) -> List[str]:
    """
    Splits an XML file into multiple XML files with a maximum number of children.

    Args:
        path (str): Path to the XML file.
        output_dir (str): Path to the output directory.
        max_children (int, optional): Maximum number of children. Defaults to 1000.

    Returns:
        List[str]: List of paths to the new XML files.
    """

    # Parse the XML
    tree = ET.parse(path)
    root = tree.getroot()
    file_name = Path(path).stem

    paths = []
    # Create new XML trees based on the split
    for idx, i in enumerate(range(0, len(root), max_children)):
        new_root = ET.Element(root.tag, root.attrib)
        new_root.extend(root[i:i + max_children])
        new_tree = ET.ElementTree(new_root)
        new_tree.write(f"{output_dir}/{file_name}_{idx}.xml")
        paths.append(f"{output_dir}/{file_name}_{idx}.xml")
    
    return paths


if __name__ == '__main__':
    paths = split_xml(
        path= "TheNewYorkTimes1985.xml",
        output_dir= "output",
        max_children= 1000
    )
    print(paths)
