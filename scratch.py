from flask import Flask, render_template, jsonify
from threading import Thread
import time
import random

app = Flask(__name__)

received_data = ""

# List of hardcoded multi-paragraph strings
hardcoded_data = [
    "The evolution of technology has been incredibly rapid in the last few decades, transforming everything from how we communicate to the way we do business. Looking ahead, we see trends like artificial intelligence and quantum computing poised to redefine the boundaries of what's possible. These technologies are not just theoretical; they are becoming more practical and accessible, promising to solve complex problems in fields like medicine, environmental science, and logistics.\nThe impact of technology on society cannot be overstated. With advancements in automation and robotics, the nature of work is changing. While some jobs may become obsolete, new opportunities are emerging in areas like AI development, data analysis, and cybersecurity. It's crucial that education systems adapt to these changes, preparing future generations for a world where technology is deeply integrated into every aspect of life.",
    "As climate change becomes a more pressing issue, the concept of sustainable living has gained significant importance. This involves adopting lifestyles and practices that reduce our environmental footprint, like minimizing waste, using renewable energy sources, and supporting sustainable agriculture. By making conscious choices about how we live, travel, and consume, we can collectively make a significant impact on the health of our planet.\nEnvironmental conservation efforts are also crucial in protecting biodiversity and natural habitats. Initiatives like reforestation, wildlife protection, and pollution reduction play a key role in preserving the planet for future generations. Governments, organizations, and individuals must work together to create policies and practices that support environmental sustainability.",
    "The world is more interconnected than ever, leading to an unprecedented exchange of cultures, ideas, and traditions. This cultural diversity enriches societies by bringing in new perspectives and fostering creativity and innovation. However, it also presents challenges in terms of integration and preserving cultural identities.\nGlobalization has facilitated this exchange, allowing people, goods, and information to move across borders more freely. While it has led to economic growth and cultural exchange, it also raises concerns about economic disparity and cultural homogenization. Balancing the benefits of globalization with the need to respect and preserve local cultures and traditions is one of the key challenges of our time.",
    "The focus on health and wellness has become increasingly prominent in modern society. With the rise of chronic diseases and mental health issues, there's a growing recognition of the importance of a holistic approach to health. This includes not just physical health, but also mental and emotional well-being.\nThe role of diet, exercise, and stress management in maintaining health cannot be overstated. Additionally, the availability of health information and medical technology has empowered individuals to take a more active role in managing their health. However, there is still a need to address disparities in healthcare access and to ensure that advancements in medical technology are available to all segments of society.",
    "The field of education is undergoing significant changes, driven by technological advancements and a changing job market. Online learning platforms, digital classrooms, and interactive educational tools are making learning more accessible and engaging. The concept of lifelong learning is also gaining traction, recognizing that education does not stop at formal schooling but is a continuous process throughout one's life.\nThese innovations are not without challenges. There is a need to ensure that educational resources are accessible to all, regardless of socioeconomic background. Additionally, educational systems must adapt to prepare students for a rapidly changing world, where skills like critical thinking, creativity, and adaptability are as important as technical knowledge.",
    "The exploration of space continues to captivate the human imagination. Recent advancements have not only deepened our understanding of the universe but also opened up possibilities for commercial space travel and even colonization of other planets. These endeavors are not just about scientific discovery; they have potential implications for resources, national security, and even the future survival of humanity.\nHowever, space exploration also raises important ethical and logistical questions. The costs involved are enormous, and the risks are high. There is a need to balance the pursuit of knowledge and adventure with responsible stewardship and consideration of the broader implications for society and the planet.",
    "Artificial Intelligence (AI) is rapidly transforming industries and societies. Its applications range from simple automation to complex problem-solving in fields like healthcare, finance, and transportation. However, as AI systems become more advanced, ethical concerns are increasingly coming to the forefront.\nIssues such as privacy, bias in AI algorithms, and the impact on employment are critical considerations. There is a growing demand for ethical frameworks and regulations to guide the development and implementation of AI technologies. Ensuring that AI benefits society as a whole, without infringing on individual rights or exacerbating inequalities, is a significant challenge for policymakers and technologists alike.",
    "The trend of urbanization is accelerating, with more people living in cities than ever before. This shift presents both challenges and opportunities. Smart cities, which use technology to improve the efficiency and quality of urban services, are seen as a key solution to the challenges posed by urbanization.\nSmart cities integrate technologies like IoT (Internet of Things), AI, and big data to manage urban infrastructure and services. This includes everything from traffic and waste management to energy usage and public safety. However, building smart cities requires careful planning, significant investment, and collaboration between various stakeholders, including governments, technology providers, and citizens."
]


def update_data():
    global received_data
    while True:
        # Randomly select a string from the list
        received_data = random.choice(hardcoded_data)
        time.sleep(0.5)  # Update every 5 seconds


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    return jsonify({'data': received_data})


if __name__ == "__main__":
    Thread(target=update_data).start()
    app.run(debug=True, host='0.0.0.0', port=5000)
