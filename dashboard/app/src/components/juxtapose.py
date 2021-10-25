from base64 import b64encode

import streamlit.components.v1 as components

from ..config import STREAMLIT_STATIC_PATH


def juxtapose(
    img1: str,
    img2: str,
    height: int = 1000,
    id: str = "foo",
    img1_label: str = "img1",
    img2_label: str = "img2",
):  # data

    """Create a new timeline component.

    Parameters
    ----------
    `height` (`int` or `None`): Height of the timeline in px

    Returns
    -------
    `static_component` (`Boolean`): Returns a static component with a timeline
    """

    # load css + js
    cdn_path = "https://cdn.knightlab.com/libs/juxtapose/latest"
    css_block = f'<link rel="stylesheet" href="{cdn_path}/css/juxtapose.css">'
    js_block = f'<script src="{cdn_path}/js/juxtapose.min.js"></script>'

    img1_extension = img1.split(".")[-1]
    img2_extension = img2.split(".")[-1]

    with open(STREAMLIT_STATIC_PATH / img1, "rb") as img1_bytes:
        with open(STREAMLIT_STATIC_PATH / img2, "rb") as img2_bytes:
            # write html block
            htmlcode = (
                css_block
                + """"""
                + js_block
                + """
                <div id="foo" style="width: 95%; height: """
                + str(height)
                + """
                px; margin: 1px;"></div>
                <script>
                slider = new juxtapose.JXSlider('#"""
                + id
                + """',
                    [
                        {
                            src: '"""
                + f"data:image/{img1_extension};base64, {b64encode(img1_bytes.read()).decode('utf-8')}"
                + """',
                            label: '"""
                + img1_label
                + """',
                        },
                        {
                            src: '"""
                + f"data:image/{img2_extension};base64, {b64encode(img2_bytes.read()).decode('utf-8')}"
                + """',
                            label: '"""
                + img2_label
                + """',
                        }
                    ],
                    {
                        animate: true,
                        showLabels: true,
                        showCredits: true,
                        startingPosition: "50%",
                        makeResponsive: true
                    });
                </script>
                """
            )
            static_component = components.html(
                htmlcode,
                height=height,
            )
            return static_component
