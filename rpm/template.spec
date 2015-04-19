Name:           ros-jade-ecto-image-pipeline
Version:        0.5.6
Release:        0%{?dist}
Summary:        ROS ecto_image_pipeline package

Group:          Development/Libraries
License:        BSD
URL:            http://plasmodic.github.io/ecto_image_pipeline/
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-jade-ecto
Requires:       ros-jade-ecto-opencv
Requires:       ros-jade-ecto-ros
Requires:       ros-jade-opencv-candidate
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-ecto
BuildRequires:  ros-jade-opencv-candidate

%description
Common tools for image based pipelines. Includes stereo and mono camera drivers,
rectification, image sinks, calibration, etc..

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Apr 19 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.6-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.5-0
- Autogenerated by Bloom

* Wed Jan 14 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.4-1
- Autogenerated by Bloom

* Wed Jan 14 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.4-0
- Autogenerated by Bloom

