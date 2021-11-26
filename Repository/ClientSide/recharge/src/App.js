import './App.css';
import  ReactDOM  from 'react-dom';
import CreatePrimaryDistributor from './components/PrimaryDis';
function App() {
  const Handlepdcreate = () =>{
    return (
      ReactDOM.render(
        <CreatePrimaryDistributor />,
        document.getElementById('root')
      )
    )
  }
  return (
    <div className="App">
      {/* <nav className="navbar">
        <a href="#">Home</a>
        <a href="#">About Us</a>
        <a href="#">Contact Us</a>
      </nav> */}
      <div id = "homerightdiv">
        <button type="button" id="jpdbutton" onClick={Handlepdcreate} >Join Primary Distributorship</button>
      </div>
    </div>
  );
}

export default App;
