/*****************************************************************************/
/*!
 *  @file   points_nodelet.cc
 *  @date   2018.12.06
 *  @author     M. Treglia Akka
 *  @brief      Definition of the Points Grid nodelet.
 *****************************************************************************/


#include <renault_lidar/nodelets/points_nodelet.h>

namespace renault_nodelets {




void PointsGrid::InitializeNodelet(){
  NODELET_INFO(" * Points Grid\t Init.");
  scan_idx_ = 0;
  frag_idx_ = 0;
  velodyne_frequency_ = 10;

  buffer_ = boost::make_shared<OrganizedPointCloudBuffer>(getPrivateNodeHandle(), 32, 12);
}


void PointsGrid::LoadRosParameters(){
  NODELET_INFO(" * Points Grid\t benchmark: %s", UseBenchmarker() ? "True" : "False");

}


void PointsGrid::EstablishRosCommunication(){
  if (UseBenchmarker())
    pack_sub_ = getNodeHandle().subscribe<velodyne_msgs::VelodynePacket>("/velodyne_packets", 100, &PointsGrid::CallbackBM, this, ros::TransportHints().tcpNoDelay());
  else
    pack_sub_ = getNodeHandle().subscribe<velodyne_msgs::VelodynePacket>("/velodyne_packets", 100, &PointsGrid::Callback, this, ros::TransportHints().tcpNoDelay());

  azimuth_pcl_publisher_ = getNodeHandle().advertise<renault_lidar::LidarAzimuths>("/velodyne_pointsgrid", 100);

  pcl_publisher_ = getNodeHandle().advertise<sensor_msgs::PointCloud2>("/velodyne_points", 100);
}




inline void PointsGrid::Callback(const velodyne_msgs::VelodynePacket::ConstPtr &pack_msg_) {
}

}
