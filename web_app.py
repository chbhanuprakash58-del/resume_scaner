# import streamlit as st
# import requests

# st.set_page_config(page_title="AI Resume Screening", layout="centered")
# st.title("📄 AI Resume Screening Bot")

# st.markdown(
#     """
# Upload your **Resume** (PDF or DOCX) and **Job Description** (PDF or DOCX), 
# and the AI will analyze the match and give you a detailed report.
# """
# )

# # Upload files
# resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
# jd_file = st.file_uploader("Upload Job Description (PDF or DOCX)", type=["pdf", "docx"])

# if st.button("Analyze Resume"):
#     if not resume_file or not jd_file:
#         st.warning("Please upload both Resume and Job Description files.")
#     else:
#         with st.spinner("Analyzing... This may take a few seconds."):
#             # Prepare files for POST request
#             files = {
#                 "resume": (resume_file.name, resume_file, resume_file.type),
#                 "jd": (jd_file.name, jd_file, jd_file.type),
#             }

#             try:
#                 # Call FastAPI endpoint
#                 response = requests.post("http://127.0.0.1:8000/analyze/", files=files)
#                 data = response.json()

#                 if response.status_code != 200 or "error" in data:
#                     st.error(data.get("error", "Unknown error occurred."))
#                 else:
#                     # Display results
#                     st.success(f"✅ Match Score: {data['match_score']}%")

#                     st.subheader("🟢 Matched Skills")
#                     st.write(", ".join(data.get("matched_skills", [])))

#                     st.subheader("🔴 Missing Skills")
#                     st.write(", ".join(data.get("missing_skills", [])))

#                     st.subheader("🧾 Summary")
#                     st.write(data.get("summary", "No summary available."))

#             except Exception as e:
#                 st.error(f"An error occurred: {str(e)}")









##### this is another genrated code###########


# import streamlit as st
# import requests
# import json

# # --- FastAPI Backend URL ---
# API_URL = "http://127.0.0.1:8000/analyze/"

# # --- Streamlit Page Setup ---
# st.set_page_config(page_title="AI Resume–JD Analyzer", page_icon="🧠", layout="centered")

# st.title("🧠 AI Resume–Job Description Analyzer")
# st.write("Upload your **Resume (PDF/DOCX)** and **Job Description (PDF/DOCX)** to analyze the match score, matched skills, and summary.")

# # --- File Uploads ---
# resume_file = st.file_uploader("📄 Upload Resume", type=["pdf", "docx"])
# jd_file = st.file_uploader("🧾 Upload Job Description", type=["pdf", "docx"])

# # --- Submit Button ---
# if st.button("🚀 Analyze"):
#     if not resume_file or not jd_file:
#         st.warning("Please upload both Resume and Job Description.")
#     else:
#         try:
#             # --- Prepare Files for API ---
#             files = {
#                 "resume": (resume_file.name, resume_file.getvalue(), resume_file.type),
#                 "jd": (jd_file.name, jd_file.getvalue(), jd_file.type),
#             }

#             # --- Send POST request to FastAPI ---
#             with st.spinner("Analyzing files... Please wait ⏳"):
#                 response = requests.post(API_URL, files=files)
            
#             # --- Handle API Response ---
#             if response.status_code == 200:
#                 result = response.json()

#                 st.success("✅ Analysis Complete!")

#                 # --- Display Results ---
#                 st.subheader("📊 Match Report")
#                 st.metric("Match Score", f"{result.get('match_score', 0)}%")

#                 st.subheader("✅ Matched Skills")
#                 matched_skills = result.get("matched_skills", [])
#                 if matched_skills:
#                     st.write(", ".join(matched_skills))
#                 else:
#                     st.write("No matched skills found.")

#                 st.subheader("⚠️ Missing Skills")
#                 missing_skills = result.get("missing_skills", [])
#                 if missing_skills:
#                     st.write(", ".join(missing_skills))
#                 else:
#                     st.write("No missing skills found.")

#                 st.subheader("🧾 Summary")
#                 st.write(result.get("summary", "No summary available."))

#             else:
#                 st.error(f"❌ API Error: {response.status_code}")
#                 st.json(response.json())

#         except Exception as e:
#             st.error(f"⚠️ Something went wrong: {e}")







############################ updated code for cresting stream lit web app###############


# import streamlit as st
# import requests
# import json
# import os

# # ------------------- CONFIGURE BACKEND URL -------------------
# # Use Render deployment URL if available, otherwise local
# API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/analyze/")

# # ------------------- STREAMLIT PAGE SETUP -------------------
# st.set_page_config(
#     page_title="AI Resume–JD Analyzer",
#     page_icon="🧠",
#     layout="centered",
# )

# st.title("🧠 AI Resume–Job Description Analyzer")
# st.write(
#     "Upload your **Resume (PDF/DOCX)** and **Job Description (PDF/DOCX)** to analyze the match score, matched skills, and summary."
# )

# # ------------------- FILE UPLOADS -------------------
# resume_file = st.file_uploader("📄 Upload Resume", type=["pdf", "docx"])
# jd_file = st.file_uploader("🧾 Upload Job Description", type=["pdf", "docx"])

# # ------------------- ANALYZE BUTTON -------------------
# if st.button("🚀 Analyze"):
#     if not resume_file or not jd_file:
#         st.warning("Please upload both Resume and Job Description.")
#     else:
#         try:
#             # Prepare files for FastAPI POST request
#             files = {
#                 "resume": (resume_file.name, resume_file.getvalue(), resume_file.type),
#                 "jd": (jd_file.name, jd_file.getvalue(), jd_file.type),
#             }

#             # Send POST request to backend
#             with st.spinner("Analyzing files... Please wait ⏳"):
#                 response = requests.post(API_URL, files=files, timeout=60)

#             # Handle API response
#             if response.status_code == 200:
#                 result = response.json()
#                 st.success("✅ Analysis Complete!")

#                 # Display match score
#                 st.subheader("📊 Match Report")
#                 st.metric("Match Score", f"{result.get('match_score', 0)}%")

#                 # Display matched skills
#                 st.subheader("✅ Matched Skills")
#                 matched_skills = result.get("matched_skills", [])
#                 if matched_skills:
#                     st.write(", ".join(matched_skills))
#                 else:
#                     st.write("No matched skills found.")

#                 # Display missing skills
#                 st.subheader("⚠️ Missing Skills")
#                 missing_skills = result.get("missing_skills", [])
#                 if missing_skills:
#                     st.write(", ".join(missing_skills))
#                 else:
#                     st.write("No missing skills found.")

#                 # Display summary
#                 st.subheader("🧾 Summary")
#                 st.write(result.get("summary", "No summary available."))

#             else:
#                 st.error(f"❌ API Error: {response.status_code}")
#                 try:
#                     st.json(response.json())
#                 except:
#                     st.write(response.text)

#         except requests.exceptions.RequestException as e:
#             st.error(f"⚠️ Connection Error: Could not reach the API. {e}")
#         except Exception as e:
#             st.error(f"⚠️ Something went wrong: {e}")






###########################  UPDATED CODE      ####################
import streamlit as st
import requests
import json
import os

# ------------------- CONFIGURE BACKEND URL -------------------
# Make sure this matches your deployed backend URL on Render
API_URL = os.getenv("API_URL", "https://resume-backend-q33z.onrender.com/analyze/")

# ------------------- STREAMLIT PAGE SETUP -------------------
st.set_page_config(page_title="AI Resume–JD Analyzer", page_icon="🧠", layout="centered")

st.title("🧠 AI Resume–Job Description Analyzer")
st.write("Upload your **Resume (PDF/DOCX)** and **Job Description (PDF/DOCX)** to check how well they match using AI.")

# ------------------- FILE UPLOAD SECTION -------------------
resume_file = st.file_uploader("📄 Upload Resume", type=["pdf", "docx"])
jd_file = st.file_uploader("🧾 Upload Job Description", type=["pdf", "docx"])

# ------------------- ANALYZE BUTTON -------------------
if st.button("🚀 Analyze"):
    if not resume_file or not jd_file:
        st.warning("⚠️ Please upload both Resume and Job Description before analyzing.")
    else:
        try:
            # Prepare files for backend
            files = {
                "resume": (resume_file.name, resume_file.getvalue(), resume_file.type),
                "jd": (jd_file.name, jd_file.getvalue(), jd_file.type),
            }

            with st.spinner("Analyzing your files... Please wait ⏳"):
                # Increased timeout to prevent Render delay
                response = requests.post(API_URL, files=files, timeout=120)

            # ------------------- RESPONSE HANDLING -------------------
            if response.status_code == 200:
                result = response.json()

                # Display results
                st.success("✅ Analysis Complete!")

                st.subheader("📊 Match Report")
                st.metric("Match Score", f"{result.get('match_score', 0)}%")

                st.subheader("✅ Matched Skills")
                matched = result.get("matched_skills", [])
                st.write(", ".join(matched) if matched else "No matched skills found.")

                st.subheader("⚠️ Missing Skills")
                missing = result.get("missing_skills", [])
                st.write(", ".join(missing) if missing else "No missing skills found.")

                st.subheader("🧾 Summary")
                st.write(result.get("summary", "No summary generated."))

            else:
                st.error(f"❌ API Error: {response.status_code}")
                try:
                    st.json(response.json())
                except:
                    st.text(response.text)

        except requests.exceptions.Timeout:
            st.error("⏱️ The request took too long and timed out. Please try again later.")
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Unable to connect to backend. Please check your backend URL or network.")
        except Exception as e:
            st.error(f"❌ Unexpected Error: {e}")
