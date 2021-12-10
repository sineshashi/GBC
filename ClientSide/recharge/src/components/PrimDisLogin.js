import { useState } from "react";
import axios from "axios";
import ReactDOM from "react-dom";
import default_profile from "./Images/default_profile.png";

const PrimDisProfile = () => {
  const [success, setSuccess] = useState("");
  const [errorData, setErrorData] = useState("");
  const [first_name, setfirst_name] = useState("");
  const [last_name, setlast_name] = useState("");
  const [email, setemail] = useState("");
  const [username, setusername] = useState("");
  const [userid, setuserid] = useState(0);
  const [id, setid] = useState(0);
  const [mobile_number, setmobile_number] = useState(0);
  const [date_of_birth, setdate_of_birth] = useState("");
  const [prim_dis_price, setprim_dis_price] = useState(0);
  const [dis_ref_code, setdis_ref_code] = useState("");
  const [ret_ref_code, setret_ref_code] = useState("");
  const [percentage, setpercentage] = useState(0);
  const [airtel_small_percentage, setairtel_small_percentage] = useState(0);
  const [image, setimage] = useState("");
  let cookies = document.cookie.split(";");
  for (var i = 0; i < cookies.length; i++) {
    let jointarray = cookies[i].split("=");
    if (jointarray[0].trim() == "accessToken") {
      var accessToken = jointarray[1].trim();
    }
  }
  axios({
    method: "get",
    url: "http://localhost:8000/primarydistributor/myprofile",
    responseType: "json",
    headers: {
      Authorization: "Bearer " + accessToken,
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      setSuccess("true");
      let responseData = response.data[0];
      setfirst_name(responseData.user.first_name);
      setlast_name(responseData.user.last_name);
      setemail(responseData.user.email);
      setusername(responseData.user.username);
      setuserid(responseData.user.id);
      setid(responseData.id);
      setmobile_number(responseData.mobile_number);
      setdate_of_birth(responseData.date_of_birth);
      setprim_dis_price(responseData.primary_dis_price);
      setdis_ref_code(responseData.distributor_referral_code);
      setret_ref_code(responseData.retailer_referral_code);
      setpercentage(responseData.percentage);
      setairtel_small_percentage(responseData.airtel_small_percentage);
    })
    .catch((error) => {
      setSuccess("false");
      setErrorData(error.response.request.responseText);
    });
  const handleProfile = () => {
    ReactDOM.render(
      <PrimaryDistributorProfile
        first_name={first_name}
        last_name={last_name}
        email={email}
        username={username}
        mobile_number={mobile_number}
        date_of_birth={date_of_birth}
        id={id}
      />,
      document.getElementById("root")
    );
  };
  if (success == "false") {
    return <h1>{errorData}</h1>;
  } else {
    return (
      <>
        <div className="profile" id="pdprofileicon" onClick={handleProfile}>
          <img src={default_profile} alt="profile" width="75px" />
          <br />
          <p id="profileiconheader" fontSize="10pt">
            {first_name + " " + last_name}
          </p>
        </div>
      </>
    );
  }
};

const PrimaryDistributorProfile = (props) => {
  const updatePersInfo = () => {
    ReactDOM.render(
      <UpdatePersonalInfo
        first_name={props.first_name}
        last_name={props.last_name}
        email={props.email}
        mobile_number={props.mobile_number}
        date_of_birth={props.date_of_birth}
        id={props.id}
      />,
      document.getElementById("root")
    );
  };
  return (
    <>
      <h1>Your personal information</h1>
      <ul>
        <li>First Name: {props.first_name}</li>
        <li>Last Name: {props.last_name}</li>
        <li>Email: {props.email}</li>
        <li>Username: {props.username}</li>
        <li>Mobile Number: {props.mobile_number}</li>
        <li>Date of birth: {props.date_of_birth}</li>
      </ul>
      <button onClick={updatePersInfo}>Update Personal Information</button>
    </>
  );
};

const UpdatePersonalInfo = (props) => {
  const [first_name, setfirst_name] = useState(props.first_name);
  const [last_name, setlast_name] = useState(props.last_name);
  const [email, setemail] = useState(props.email);
  const [mobile_number, setmobile_number] = useState(props.mobile_number);
  const [date_of_birth, setdate_of_birth] = useState(props.date_of_birth);
  const handleFirstName = (e) => {
    setfirst_name(e.target.value);
  };
  const handleLastName = (e) => {
    setlast_name(e.target.value);
  };
  const handleEmail = (e) => {
    setemail(e.target.value);
  };
  const handleDateOfBirth = (e) => {
    setdate_of_birth(e.target.value);
  };
  const handleMobileNumber = (e) => {
    setmobile_number(e.target.value);
  };
  const updateData = () => {
    let cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      let jointarray = cookies[i].split("=");
      if (jointarray[0].trim() == "accessToken") {
        var accessToken = jointarray[1].trim();
      }
    }
    axios({
      method: "put",
      url:
        "http://localhost:8000/primarydistributor/updateprofile/" +
        props.id.toString(),
      data: JSON.stringify({
        user: {
          first_name: first_name,
          last_name: last_name,
          email: email,
        },
        mobile_number: mobile_number,
        date_of_birth: date_of_birth,
      }),
      responseType: "json",
      headers: {
        Authorization: "Bearer " + accessToken,
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        ReactDOM.render(
          <h1>Your profile has been updated.</h1>,
          document.getElementById("root")
        );
      })
      .catch((error) => {
        ReactDOM.render(<h1>{error.response.request.responseText}</h1>);
      });
  };
  return (
    <>
      <h1>Please give the info to be updated</h1>
      <div className="primaryhead" id="updatedPersonalInfo">
        <label htmlFor="first_name">First Name </label>
        <input
          type="text"
          className="updatePrimaryInput"
          name="first_name"
          id="first_name"
          placeholder={first_name}
          value={first_name}
          onChange={handleFirstName}
        />{" "}
        <br />
        <br />
        <label htmlFor="last_name">Last Name </label>
        <input
          type="text"
          className="updatePrimaryInput"
          name="last_name"
          id="last_name"
          placeholder={last_name}
          value={last_name}
          onChange={handleLastName}
        />{" "}
        <br />
        <br />
        <label htmlFor="email">Email </label>
        <input
          type="email"
          className="updatePrimaryInput"
          name="email"
          id="email"
          placeholder={email}
          value={email}
          onChange={handleEmail}
        />{" "}
        <br />
        <br />
        <label htmlFor="mobile_number">Mobile Number </label>
        <input
          type="number"
          className="updatePrimaryInput"
          name="mobile_number"
          id="mobile_number"
          placeholder={mobile_number}
          value={mobile_number}
          onChange={handleMobileNumber}
        />{" "}
        <br />
        <br />
        <label htmlFor="date_of_birth">Date Of Birth </label>
        <input
          type="date"
          className="updatePrimaryInput"
          name="date_of_birth"
          id="date_of_birth"
          placeholder={date_of_birth}
          value={date_of_birth}
          onChange={handleDateOfBirth}
        />{" "}
        <br />
        <br />
        <button type="button" onClick={updateData}>
          Update
        </button>
      </div>
    </>
  );
};

export default PrimDisProfile;
