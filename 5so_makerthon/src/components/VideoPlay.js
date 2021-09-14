import React,{Component} from "react";
import ReactPlayer from 'react-player';
import "../components/styles/VideoPlay.css";


class VideoPlay extends Component {
    render() {
        return (
            
        <div className='player-wrapper'>          
        <ReactPlayer
        className='react-player fixed-bottom'
        url= 'normal_action.MP4'
        width='70%'
        height='70%'
        controls= {true}
        />        
        </div> 
        )
    }
}

export default VideoPlay;