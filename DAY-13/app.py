import gradio as gr
import pickle

clf = pickle.load(open("model.pkl", "rb"))

def predict(iq, cgpa):
    print(iq, cgpa)
    result = clf.predict([[cgpa, iq]])

    if result[0] == 1:
        return "Placement Ho Jayega"
    return "Placement Nahi Hoga"


with gr.Blocks(title="Placement Predictor", theme=gr.themes.Default()) as demo:
    gr.Markdown("# Placement Predictor")
    iq = gr.Number(label="IQ of the student")
    cgpa = gr.Number(label="CGPA of the student")

    predict_btn = gr.Button("Predict", variant="primary")
    prediction = gr.Text(label="Prediction")

    predict_btn.click(fn=predict, inputs=[iq, cgpa], outputs=[prediction])


demo.launch()