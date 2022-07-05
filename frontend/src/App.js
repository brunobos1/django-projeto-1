import { Routes, Route } from "react-router-dom";
import Login from "./Login";
import Profile from "./Profile";
import { RequireToken } from "./Auth";
import Signup from "./Signup";

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
