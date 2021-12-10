import { useState } from "react";
import axios from "axios";
import ReactDOM from "react-dom";
import PrimDisProfile from "./PrimDisLogin";

const Login = () => {
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
  const handleusername = (e) => {
    setusername(e.target.value);
  };
  const handlepassword = (e) => {
    setpassword(e.target.value);
  };
  const handleClick = () => {
    let request_data = JSON.stringify({
      username: username,
      password: password,
    });
    axios({
      method: "post",
      url: "http://localhost:8000/login/",
      data: request_data,
      responseType: "json",
      timeout: 5000,
      headers: {
        "Content-Type": "application/json",
        accept: "application/json",
      },
    })
      .then((response) => {
        let d = new Date();
        document.cookie =
          "accessToken=" +
          response.data.access +
          "; max-age=" +
          30 * 24 * 60 * 60 +
          "; expires=" +
          new Date(d.getTime + 30 * 24 * 60 * 60 * 1000);
        ReactDOM.render(<PrimDisProfile />, document.getElementById("root"));
      })
      .catch((error) => {
        ReactDOM.render(
          <>
            <h1>{error.response.request.responseText}</h1>
          </>,
          document.getElementById("root")
        );
      });
  };
  return (
    <>
      <div className="loginHead">
        <h1>Please enter the following details to log into your account:</h1>
      </div>
      <div className="body">
        <label htmlFor="username">username</label>
        <input
          type="username"
          id="username"
          placeholder="username"
          name="username"
          value={username}
          onChange={handleusername}
        />
        <br />
        <br />
        <label htmlFor="password">password</label>
        <input
          type="password"
          id="password"
          placeholder="password"
          name="password"
          value={password}
          onChange={handlepassword}
        />
        <br />
        <br />
        <button id="loginbutton" onClick={handleClick}>
          {" login "}
        </button>
      </div>
    </>
  );
};

export default Login;
