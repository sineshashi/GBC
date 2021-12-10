import "./App.css";
import ReactDOM from "react-dom";
import CreatePrimaryDistributor from "./components/PrimaryDis";
import PrimDisProfile from "./components/PrimDisLogin";
import Login from "./components/log_in";
import Logout from "./components/log_out";
function App() {
  const Handlepdcreate = () => {
    return ReactDOM.render(
      <CreatePrimaryDistributor />,
      document.getElementById("root")
    );
  };
  const HandlePDLogin = () => {
    let cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      let jointarray = cookies[i].split("=");
      var keyarray = new Array();
      keyarray[i] = jointarray[0].trim();
    }
    if (keyarray.indexOf("accessToken") == -1) {
      return ReactDOM.render(<Login />, document.getElementById("root"));
    } else {
      return ReactDOM.render(
        <PrimDisProfile />,
        document.getElementById("root")
      );
    }
  };
  const Handlelogout = () =>{
    ReactDOM.render(
      <Logout />,
      document.getElementById("root")
    )
  }
  return (
    <div className="App">
      {/* <nav className="navbar">
        <a href="#">Home</a>
        <a href="#">About Us</a>
        <a href="#">Contact Us</a>
      </nav> */}
      <div id="homerightdiv">
        <button type="button" id="jpdbutton" onClick={Handlepdcreate}>
          Join Primary Distributorship
        </button>
        <button type="button" id="pdloginbutton" onClick={HandlePDLogin}>
          Primary Distributor Login
        </button>
      </div>
      <button type="button" id="logoutbtn" onClick={Handlelogout}> Log out </button>
    </div>
  );
}

export default App;
