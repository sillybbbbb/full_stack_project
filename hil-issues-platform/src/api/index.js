import axios from '~/axios'

export function getStatistics1(){
    return axios.get("/data/asset/data/aqi-beijing.json")
}
