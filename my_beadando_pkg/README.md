# my_beadando_pkg – kis beadandó

Egyszerű ROS2 Python csomag egy publisherrel és egy subscriberrel.
A publisher fél másodpercenként üzen a **/kisbeadando_chatter** topikra,
a subscriber kiírja a kapott üzeneteket.

## Követelmények
- ROS2
- colcon, Python 3

## Build
```bash
cd ~/ros2_ws
colcon build --packages-select my_beadando_pkg

cat > ~/ros2_ws/src/my_beadando_pkg/README.md << 'EOF'
# my_beadando_pkg – kis beadandó

Egyszerű ROS2 Python csomag egy publisherrel és egy subscriberrel.
A publisher fél másodpercenként üzen a **/kisbeadando_chatter** topikra,
a subscriber kiírja a kapott üzeneteket.

## Követelmények
- ROS2
- colcon, Python 3

## Build
```bash
cd ~/ros2_ws
colcon build --packages-select my_beadando_pkg









