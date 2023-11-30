import { useState } from 'react'
import Modal from 'react-modal'

import './App.css'

Modal.setAppElement('#root');

function LoginModal({isOpen, onClose}){
  const [issue, setIssue] = useState(
    {
      id : "",
      pw : "", 
    }
  )

  const hSubmit=(e)=>{
    e.preventDefault();

    console.log("issue", {issue})

    setTimeout(() => {
      window.alert('Successfully submitted!');
    }, 500)
    onClose()    
  }

  const customModalStyles = { // 로그인 팝업창 디자인
    content: {
      backgroundColor: '#646cffaa', // Dark background color
      color: '#fff', // Light text color
      border: 'none',
      borderRadius: '0px', // 모서리 둥근 정도
      maxWidth: '500px', // 가로
      maxHeight: '350px', // 세로
      margin: 'auto', 
      padding: '20px',
    },

    overlay: {
      backgroundColor: 'rgba(0, 0, 0, 0.5)', // Dark overlay
    },

  };

  return (
    <>
      <Modal isOpen={isOpen}
        onRequestClose={onClose}
        shouldCloseOnOverlayClick={false}
        
        style={customModalStyles}>
          
          <form onSubmit={hSubmit}>

            <div>
              <label>ID : </label>
              <input
                type='text'
                value={issue.id}
                onChange={(e)=>setIssue(prev=>({...prev, id:e.target.value}))}
              ></input>
            </div>

            <div>
              <label>PW : </label>
              <input
              type='text'
              value={issue.pw}
              onChange={(e)=>setIssue(prev=>({...prev, pw:e.target.value}))}></input>
            </div>

            <button type='submit' style={{margin: '8px'}}>Login</button>
            <button onClick={onClose}>Close</button>

          </form>

      </Modal>

    </>
  )
}

function SignUpModal({isOpen, onClose}){
  const [issue, setIssue] = useState(
    {
      name : "",
      id : "", 
      pw : "",
      tel : "",
      grade : ""
    }
  )

  const hSubmit=(e)=>{
    e.preventDefault();

    console.log("issue", {issue})

    setTimeout(() => {
      window.alert('Successfully submitted!');
    }, 500)
    onClose()    
  }

  const customModalStyles = { // 회원가입 팝업창 디자인
    content: {
      backgroundColor: '#646cffaa', // Dark background color
      color: '#fff', // Light text color
      border: 'none',
      borderRadius: '0px', // 모서리 둥근 정도
      maxWidth: '500px', // 가로
      maxHeight: '350px', // 세로
      margin: 'auto', 
      padding: '20px',
    },

    overlay: {
      backgroundColor: 'rgba(0, 0, 0, 0.5)', // Dark overlay
    },

  };

  return (
    <>
      <Modal isOpen={isOpen}
        onRequestClose={onClose}
        shouldCloseOnOverlayClick={false}
        
        style={customModalStyles}>
          
          <form onSubmit={hSubmit}>

            <div>
              <label>Name : </label>
              <input
                type='text'
                value={issue.name}
                onChange={(e)=>setIssue(prev=>({...prev, name:e.target.value}))}
              ></input>
            </div>

            <div>
              <label>ID : </label>
              <input
              type='text'
              value={issue.id}
              onChange={(e)=>setIssue(prev=>({...prev, id:e.target.value}))}></input>
            </div>

            <div>
              <label>PW : </label>
              <input
              type='text'
              value={issue.pw}
              onChange={(e)=>setIssue(prev=>({...prev, pw:e.target.value}))}></input>
            </div>

            <div>
              <label>전화번호 : </label>
              <input
              type='tel'
              value={issue.tel}
              onChange={(e)=>setIssue(prev=>({...prev, tel:e.target.value}))}></input>
            </div>

            <div>
            <label>급수 : </label>
              <select>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="C">C</option>
                <option value="D">D</option>
              </select>
            </div>

            <button type='submit' style={{margin: '8px'}}>SignUp</button>
            <button onClick={onClose}>Close</button>

          </form>

      </Modal>

    </>
  )
}

function App(){ // npm start 했을 때 나타나는 화면
  const [loginModalOpen, setLoginModalOpen] = useState(false)
  const [signupModalOpen, setSignupModalOpen] = useState(false)

  const openLoginModal=() =>{
    setLoginModalOpen(true);
    setSignupModalOpen(false);
  }

  const openSignupModal=() =>{
    setLoginModalOpen(false);
    setSignupModalOpen(true);
  }

  const closeModal=() =>{
    setLoginModalOpen(false);
    setSignupModalOpen(false);
  }

  return(
    
  <>

    <div id="left">
      <div style={{ backgroundColor: 'midnightblue', width: '500px', height: '1300px', paddingTop: '1%', opacity: '92%' }}>


      <div class="prof_img">
          <img src="https://blog.kakaocdn.net/dn/d9DBmO/btrShHIWImK/bd7vHKU1N0eUoLLE6ETBwK/img.png"
              alt="Logo" width="300" height="300" class="d-inline-block align-text-top"></img>
      </div>

      <div style={{ textAlign : 'center', marginTop: '40px' }}><h3>연세 동아리인을 위한 포탈</h3></div>

          <h1><b>Yonsei Dongari Portal</b></h1>
      
          <button type="button" class="btn btn-warning" onClick={openLoginModal}><h4><b><a href = "login/" >로그인 (Login)</a></b></h4></button>
          <p>

          </p>
          <button type="button" class="btn btn-outline-light" onClick={openSignupModal}><h5><b><a href = "signup/">회원가입 (Signup)</a></b></h5></button>

          <LoginModal isOpen={loginModalOpen} onClose={closeModal}/>
          <SignUpModal isOpen={signupModalOpen} onClose={closeModal}/>

      </div>

    </div>

    <div id="right">
      <div style={{ backgroundColor: 'white', width: '900px', height: '1300px', paddingTop: '1px', opacity: '93%' }}>

          <div style={{ margin : '50px', paddingRight: '100%' }}>
              <div style={{ textDecoration: 'underline' }}><h1><b>SERVICE</b></h1></div>


              {/* 공지사항 부분 ! */}
              <div style={{ width: '720px', height: '100px', textAlign: 'left', paddingTop: '15px' }}>
                  <div class="card">
                      <div class="card-header"><h4><b>Notice</b></h4></div>

                          <div class="card-body">

                              
                              {/* <h8>여기에 공지사항 내용 넣기</h8>
                              <div style="text-align: justify"><h8>여기에 공지사항 내용 넣기</h8></div>
                               */}

                              <ul class="list-group list-group-flush">
                                  <li class="list-group-item">공지사항 넣기</li>
                                  <li class="list-group-item">공지사항 넣기</li>
                              </ul>

                              <div style={{ textAlign: 'right' }}> 
                                  {/* <a href="#" class="btn btn-primary">+</a> */}
                              </div>

                          </div>
                  </div>
              </div>

              {/* application 버튼
              <div style="padding-top: 70px">
                  <button type="button" class="btn btn-outline-secondary btn-sm"><h4><b>Notice</b></h4></button>
              </div> */}
              



              {/* Application 부분 ! */}
              <div style={{paddingTop: '140px', paddingLeft: '11px' }}><h4><b>Application</b></h4></div>

              {/* 동아리 가입! */}
              <div style={{ paddingLeft: '10px' }}>
                  <button type="button" class="btn btn-outline-secondary btn-sm"><h4><b>동아리 가입</b></h4></button>
              </div>


              {/* 정기활동 신청! */}
              <div style={{ position: 'absolute', left: '319px', top: '384px' }}>
                  <button type="button" class="btn btn-outline-secondary btn-sm"><h4><b>정기활동 신청</b></h4></button>
              </div>




              {/* Community 부분 ! */}
              <div style={{ paddingTop: '25px', paddingLeft: '11px' }}><h4><b>Community</b></h4></div>

              {/*  자유 게시판! */}
              <div style={{ paddingLeft: '10px' }}>
                  <button type="button" class="btn btn-outline-secondary btn-sm"><h4><b>자유 게시판</b></h4></button>
              </div>



              {/* 홍보 게시판! */}
              <div style={{ position: 'absolute', left: '319px', top: '556px' }}>
                  <button type="button" class="btn btn-outline-secondary btn-sm"><h4><b>홍보 게시판</b></h4></button>
              </div>


              {/* 택시 게시판! */}
              <div style={{ position: 'absolute', left: '580px', top: '556px' }}>
                  <button type="button" class="btn btn-outline-secondary btn-sm"><h4><b>택시 게시판</b></h4></button>
              </div>

          </div>

      </div>

    </div>

  </>           

  )
}

export default App