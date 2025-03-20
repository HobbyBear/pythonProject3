from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dealvideo', methods=['POST'])
def process():
    """
    处理来自客户端的POST请求，解析请求体中的JSON数据，
    并从中提取所需的参数进行处理。
    """
    if not request.is_json:
        return jsonify({"error": "Request body must be a JSON object"}), 400

    try:
        body_json = request.get_json()

        # 从请求体中提取参数
        input_video = body_json.get('input_video')
        output_video = body_json.get('output_video')
        target_duration = body_json.get('target_duration', 20)  # 默认目标视频时长为20秒
        rotationtype = body_json.get('rotationtype')
        rotate_video = body_json.get('rotate_video')
        output_image_path = body_json.get('output_image_path')
        remoteurl = output_video
        ossresult = body_json.get('ossresult')
        osscover = body_json.get('osscover')

        # 在这里添加你的业务逻辑处理代码
        # 示例：打印接收到的参数
        print(f"Input Video: {input_video}")
        print(f"Output Video: {output_video}")
        print(f"Target Duration: {target_duration}")
        print(f"Rotation Type: {rotationtype}")
        print(f"Rotate Video: {rotate_video}")
        print(f"Output Image Path: {output_image_path}")
        print(f"Remote URL: {remoteurl}")
        print(f"OSS Result: {ossresult}")
        print(f"OSS Cover: {osscover}")

        # 返回成功的响应
        return jsonify({
            "message": "Processing completed successfully",
            "input_video": input_video,
            "output_video": output_video,
            "target_duration": target_duration,
            "rotationtype": rotationtype,
            "rotate_video": rotate_video,
            "output_image_path": output_image_path,
            "remoteurl": remoteurl,
            "ossresult": ossresult,
            "osscover": osscover
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)