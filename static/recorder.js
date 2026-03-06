let mediaRecorder;
let audioChunks = [];

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();
            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };
        });
}

function stopRecording() {
    mediaRecorder.stop();
    mediaRecorder.onstop = () => {
        const blob = new Blob(audioChunks, { type: 'audio/wav' });
        const file = new File([blob], "answer.wav");
        const container = new DataTransfer();
        container.items.add(file);
        document.getElementById('audioFile').files = container.files;
        document.getElementById('audioForm').submit();
    };
}
