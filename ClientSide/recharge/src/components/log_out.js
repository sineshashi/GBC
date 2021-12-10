const Logout = () => {
  document.cookie = "accessToken=; max-age=" + 0 + "; expires=" + new Date();
  return (
      <>
        <h1>You have been logged out.</h1>
      </>
  )
};
export default Logout