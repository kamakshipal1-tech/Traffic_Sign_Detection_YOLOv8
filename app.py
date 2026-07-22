import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Traffic Sign Detection",
    page_icon="🚦",
    layout="wide"
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🚦 Traffic Sign Detection")

st.sidebar.markdown("""
### About

This application detects traffic signs using a custom-trained **YOLOv8** model.

### Features

- Upload any road image
- Detect traffic signs
- Bounding boxes
- Confidence scores

---

**Model:** YOLOv8

**Framework:** Ultralytics

**Deployment:** Streamlit
""")

confidence = st.sidebar.slider(
    "Confidence Threshold",
    min_value=0.05,
    max_value=1.0,
    value=0.25,
    step=0.05
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚦 Traffic Sign Detection using YOLOv8")

st.write(
    "Upload a road image to detect traffic signs using a custom-trained YOLOv8 model."
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# --------------------------------------------------
# FILE UPLOADER
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------------------------
# MAIN
# --------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file.name)
        temp_path = temp_file.name

    if st.button("🚦 Detect Traffic Signs", use_container_width=True):

        with st.spinner("Running YOLOv8..."):

            results = model.predict(
                source=temp_path,
                conf=confidence,
                save=False
            )

        result = results[0]

        with col2:
            st.subheader("Detection Result")
            st.image(result.plot(), use_container_width=True)

        boxes = result.boxes

        st.markdown("---")

        st.subheader("📊 Detection Summary")

        if len(boxes) == 0:

            st.warning("No traffic signs detected.")

        else:

            st.success(f"Detected {len(boxes)} object(s).")

            for i, box in enumerate(boxes):

                cls = int(box.cls[0])
                conf = float(box.conf[0])

                st.write(
                    f"**{i+1}. {model.names[cls]}** "
                    f"— Confidence: **{conf:.2%}**"
                )

    os.remove(temp_path)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Developed using Streamlit + YOLOv8 + Ultralytics"
)