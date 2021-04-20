from __future__ import annotations

from page_xml_draw.gends.page import parse, GeneratedsSuper, PcGtsType


class XmlTag:
    name: str
    elements: list[GeneratedsSuper]

    def __init__(self, name: str, elements: list[GeneratedsSuper]) -> XmlTag:
        self.name = name
        self.elements = elements


class XmlTraverser:
    pcgts: PcGtsType
    focused: XmlTag
    previous: list[XmlTag]

    def __init__(self, instring: str) -> XmlTag:
        self.pcgts = parse(instring, silence=True)
        self.focused = XmlTag("PcGts", [self.pcgts])
        self.previous = []

    def focus_on_children(self, name: str) -> None:
        self.previous.append(self.focused)

        children = []

        for element in self.focused.elements:
            getter = getattr(element, "get_" + name)
            child = getter()

            if isinstance(child, list):
                children += child
            else:
                children.append(child)

        self.focused = XmlTag(name, children)

    def focus_on_parents(self) -> None:
        self.focused = self.previous.pop()
