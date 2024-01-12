import streamlit as st
import ffmpeg
import os
from tempfile import NamedTemporaryFile

def compress_video(input_path, output_path, bitrate, codec, preset):
    (
        ffmpeg
        .input(input_path)
        .output(output_path, video_bitrate=bitrate, vcodec=codec, preset=preset, pix_fmt='yuv420p')
        .run(overwrite_output=True)
    )

def main():
    st.title("Video Compressor")

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file is not None:
        with NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            input_path = temp_file.name

        st.video(input_path)

        # User input for compression settings
        bitrate = st.text_input("Bitrate (e.g., 1M, 500k)", value="1M")
        codec = st.selectbox("Codec", ["libx264", "libx265", "mpeg4"])
        preset = st.selectbox("Compression Preset", ["ultrafast", "fast", "medium", "slow"])

        if st.button('Compress Video'):
            output_path = input_path.split('.')[0] + '_compressed.mp4'
            compress_video(input_path, output_path, bitrate, codec, preset)

            with open(output_path, "rb") as file:
                btn = st.download_button(
                        label="Download Compressed Video",
                        data=file,
                        file_name="compressed_video.mp4",
                        mime="video/mp4"
                    )

            os.remove(output_path)  # Clean up the temporary file

        os.remove(input_path)  # Clean up the input file

if __name__ == "__main__":
    main()
