import React from 'react';
import "./styles/LivePlay.css";

const getWebcam = (callback) => {
  try {
    const constraints = {
      'video': true,
      'audio': false
    }
    navigator.mediaDevices.getUserMedia(constraints)
      .then(callback);
  } catch (err) {
    console.log(err);
    return undefined;
  }
}

const Styles = {
  Video: { width: "100%", height: "60%", background: '#536349'},
  None: { display: 'none' },
}


function LivePlay() {
    const [playing, setPlaying] = React.useState(undefined);
  
    const videoRef = React.useRef(null);
  
    React.useEffect(() => {
      getWebcam((stream => {
        setPlaying(true);
        videoRef.current.srcObject = stream;
      }));
    }, []);
  
    const startOrStop = () => {
      if (playing) {
        const s = videoRef.current.srcObject;
        s.getTracks().forEach((track) => {
          track.stop();
        });
      } else {
        getWebcam((stream => {
          setPlaying(true);
          videoRef.current.srcObject = stream;
        }));
      }
      setPlaying(!playing);
    }
  
    return (<>
      <div style={{ width: '100vw', height: '100vh', padding: '0px' }}>
        <video ref={videoRef} autoPlay style={Styles.Video} />
        <button  color="warning"  onClick={() => startOrStop()}>{playing ? 'Stop' : 'Start'} </button>
      </div >
    </>);
  }
  
  export default LivePlay;