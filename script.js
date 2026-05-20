// ① HTML에서 필요한 요소들을 가져옵니다
const nameInput   = document.getElementById("nameInput");   // 이름 입력창
const startButton = document.getElementById("startButton"); // 실습 시작 버튼
const resultArea  = document.getElementById("resultArea");  // 메시지를 표시할 영역

// ② 필수 요소가 없으면 콘솔에 경고를 남기고 실행을 멈춥니다 (방어 코드)
if (!nameInput || !startButton || !resultArea) {
  console.error("필요한 HTML 요소를 찾지 못했습니다. id 이름을 확인하세요.");
}

// ③ 메시지를 화면에 표시하는 함수
//    text: 보여줄 문장,  type: "success" 또는 "warning" (CSS 클래스 이름)
function showMessage(text, type) {
  if (!resultArea) return; // 요소가 없으면 함수를 바로 종료

  resultArea.innerHTML = ""; // 이전 메시지를 지웁니다

  const messageBox = document.createElement("div"); // 새 div를 만들고
  messageBox.className = type;                       // CSS 클래스를 붙이고
  messageBox.textContent = text;                     // 텍스트를 넣습니다

  resultArea.appendChild(messageBox); // 화면에 추가합니다
}

// ④ 버튼을 클릭했을 때 실행되는 함수
function handleStartClick() {
  if (!nameInput) return; // 입력창이 없으면 종료

  const name = nameInput.value.trim(); // 앞뒤 공백 제거 후 값을 가져옵니다

  if (name) {
    // 이름이 있으면 성공 메시지
    showMessage(`${name}님, 환영합니다! AI 협업 개발 실습을 시작합니다.`, "success");
  } else {
    // 이름이 비어 있으면 경고 메시지
    showMessage("이름을 먼저 입력해주세요.", "warning");
  }
}

// ⑤ 버튼에 클릭 이벤트를 연결합니다
if (startButton) {
  startButton.addEventListener("click", handleStartClick);
}
