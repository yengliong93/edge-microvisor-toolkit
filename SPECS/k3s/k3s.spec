Name:           k3s
Summary:        K3s - Lightweight Kubernetes
Version:        v1.32.4+k3s1
Release:        1%{?dist}
License:        ASL 2.0
Vendor:         Cloud Native Computing Foundation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://k3s.io/
Source0: https://github.com/k3s-io/k3s/archive/refs/tags/%{version}.tar.gz
Source1: https://github.com/k3s-io/k3s/releases/download/%{version}/k3s-airgap-images-amd64.tar.zst
Patch0: local.patch
BuildRequires: make
BuildRequires: docker

%description
K3s - Lightweight Kubernetes %{version}

%package        k3s
Summary:        K3s - Lightweight Kubernetes

%prep
%autosetup -Sgit

# Build the K3s binary locally using the upstream Makefile target.
%build
make local

%install
mkdir -p %{topdir}/usr/local/bin
install -m 0755 dist/artifacts/k3s %{topdir}/usr/local/bin/k3s

mkdir %{topdir}/opt
install -m 0755 install.sh %{topdir}/opt/install.sh

mkdir -p %{topdir}/var/lib/rancher/k3s/agent/images
install -m 0644 %{SOURCE1} %{topdir}/var/lib/rancher/k3s/agent/images/k3s-airgap-images-amd64.tar.zst

%post
%{topdir}/opt/install.sh

%files
/usr/local/bin/k3s
/opt/install.sh
/var/lib/rancher/k3s/agent/images/k3s-airgap-images-amd64.tar.zst