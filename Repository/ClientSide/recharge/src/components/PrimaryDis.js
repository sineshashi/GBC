import { useState } from "react";



const CreatePrimaryDistributor = () => {
  const [user, setUser] = useState({
    first_name: "",
    last_name: "",
    email: "",
    username: "",
    password: "",
    confirm_password: "",
  });
  const [first_name, setfirst_name] = useState("");
  const [last_name, setlast_name] = useState("");
  const [email, setemail] = useState("");
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
  const [confirm_password, setconfirm_password] = useState("");
  const [mobile_number, setmobile_number] = useState();
  const [date_of_birth, setdate_of_birth] = useState();
  const [image, setimage] = useState(null);
  const handleFirstName = (e) => {
    setfirst_name(e.target.value);
  };
  const handleLastName = (e) => {
    setlast_name(e.target.value);
  };
  const handleEmail = (e) => {
    setemail(e.target.value);
  };
  const handleUsername = (e) => {
    setusername(e.target.value);
  };
  const handlePassword = (e) => {
    setpassword(e.target.value);
  };
  const handleConfirmPassword = (e) => {
    setconfirm_password(e.target.value);
  };
  const handleMobileNumber = (e) => {
    setmobile_number(e.target.value);
  };
  const handleDOB = (e) => {
    setdate_of_birth(e.target.value);
  };
  const handleImage = (e) => {
    setimage(e.target.value);
  };
  
  const submitPrimaryDistributor = (e) => {
    setUser({
        first_name: first_name,
        last_name: last_name,
        email: email,
        username: username,
        password: password,
        confirm_password: confirm_password,
      })
    const createpdxhr = new XMLHttpRequest();
    createpdxhr.open("POST", "http://127.0.0.1:8000/primarydistributor", true)
  };
  

  return (
    <>
      <div>
        <h1 className="primaryhead" id="primaryhead1">
          Please enter the following details to become our Primary Distributor
        </h1>
      </div>
      <div className="body">
        <label htmlFor="first_name">First Name </label>
        <input
          type="text"
          id="first_name"
          name="first_name"
          placeholder="First Name"
          value={first_name}
          onChange={handleFirstName}
        />
        <br />
        <br />
        <label htmlFor="last_name">Last Name </label>
        <input
          type="text"
          id="last_name"
          name="last_name"
          placeholder="Last Name"
          value={last_name}
          onChange={handleLastName}
        />
        <br />
        <br />
        <label htmlFor="email">Email </label>
        <input
          type="email"
          id="email"
          name="email"
          placeholder="email"
          value={email}
          onChange={handleEmail}
        />
        <br />
        <br />
        <label htmlFor="username">username </label>
        <input
          type="text"
          id="username"
          name="username"
          placeholder="Enter a username"
          value={username}
          onChange={handleUsername}
        />
        <br />
        <br />
        <label htmlFor="password">Password </label>
        <input
          type="password"
          id="password"
          name="password"
          placeholder="Password"
          value={password}
          onChange={handlePassword}
        />
        <br />
        <br />
        <label htmlFor="confirm_password">Confirm Password </label>
        <input
          type="password"
          id="confirm_password"
          name="confirm_password"
          placeholder="Input the same password"
          value={confirm_password}
          onChange={handleConfirmPassword}
        />
        <br />
        <br />
        <label htmlFor="mobile_number">Mobile Number </label>
        <input
          type="number"
          id="mobile_number"
          name="mobile_number"
          placeholder="Mobile Number"
          value={mobile_number}
          onChange={handleMobileNumber}
        />
        <br />
        <br />
        <label htmlFor="date_of_birth">Date Of Birth </label>
        <input
          type="date"
          id="date_of_birth"
          name="date_of_birth"
          placeholder="Date of bith"
          value={date_of_birth}
          onChange={handleDOB}
        />
        <br />
        <br />
        <div>
          <img src={image} alt="preview image" />
          <input type="file" value={image} onChange={handleImage} />
        </div>
        <br />
        <br />
        <button id="pdsubtn" width="20px"> submit </button>
      </div>
    </>
  );
};

export default CreatePrimaryDistributor;
