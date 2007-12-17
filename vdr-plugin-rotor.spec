
%define plugin	rotor
%define name	vdr-plugin-%plugin
%define version	0.1.4
%define rel	13

Summary:	VDR plugin: DiseqC motor steering
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://home.vrweb.de/~bergwinkl.thomas/
Source:		vdr-%plugin-%version.tar.bz2
Patch0:		vdr-rotor-0.1.4-fix-crash.patch
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
With this plugin you can control a diseqc motor.

%prep
%setup -q -n %plugin-%version
%patch0 -p0 -b .crash

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


