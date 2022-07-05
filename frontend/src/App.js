import { Routes, Route } from "react-router-dom";
import Login from "./Login";
import Profile from "./Profile";
import { RequireToken } from "./Auth";
import Signup from "./Signup";
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyBcuuVNUSXyCIusOsF7OnbgAlFI54TGdqs",
  authDomain: "aplicacao-1-login.firebaseapp.com",
  projectId: "aplicacao-1-login",
  storageBucket: "aplicacao-1-login.appspot.com",
  messagingSenderId: "681222043652",
  appId: "1:681222043652:web:2f6d28eff86315edcf9d51",
  measurementId: "G-K2NQ8XVWY0"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

function App() {
  return (
    <div className ="App">
    <Routes>
      <Route path="/" element = {<Login/>}/>
      <Route path="/profile" 
        element={
            <RequireToken>
              <Profile />
            </RequireToken>
          }
        />
      <Route path="/signup" 
        element={
            
              <Signup />
            
          }
        />
    </Routes>
    </div>
  );
}

export default App;
