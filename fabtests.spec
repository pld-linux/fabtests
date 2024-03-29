Summary:	Test suite for libfabric API
Summary(pl.UTF-8):	Zestaw testów dla API libfabric
Name:		fabtests
Version:	1.15.1
Release:	1
License:	BSD or GPL v2
Group:		Libraries
#or https://github.com/ofiwg/fabtests/releases
#Source0Download: https://github.com/ofiwg/libfabric/releases
Source0:	https://github.com/ofiwg/libfabric/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	43d287d071958d99db4ceaea88a5477b
URL:		https://github.com/ofiwg/fabtests
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.11
BuildRequires:	libfabric-devel >= 1.15.1
BuildRequires:	libtool >= 2:2
BuildRequires:	sed >= 4.0
Requires:	libfabric >= 1.15.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fabtests provides a set of examples that uses libfabric - a
high-performance fabric software library.

%description -l pl.UTF-8
Fabtests to zbiór przykładów wykorzystujących libfabric - bibliotekę
wysoko wydajnych usług sieci typu fabric.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,/usr/bin/python3,' scripts/runfabtests.py
%{__sed} -i -e '1s,/usr/bin/env ruby,/usr/bin/ruby,' scripts/rft_yaml_to_junit_xml

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# don't package plain unit tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/fi_{av_test,cm_data,cntr_test,cq_data,cq_test,dgram,dgram_waitset,dom_test,eq_test,getinfo_test,mr_cache_evict,mr_test,msg,msg_epoll,msg_sockets,poll,rdm,rdm_atomic,rdm_rma_*,rdm_tagged_peek,scalable_ep,shared_ctx}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/runfabtests.sh
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/fi_{av_test,cm_data,cntr_test,cq_data,cq_test,dgram,dgram_waitset,dom_test,eq_test,getinfo_test,mr_test,msg,msg_epoll,msg_sockets,poll,rdm,rdm_atomic,rdm_rma_*,rdm_tagged_peek,scalable_ep,shared_ctx}.1

# adjust names for 1.15.x
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/fi_efa_{ep_rnr_retry,rnr_queue_resend}.1
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/fi_{inj_complete,msg_inject}.1*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/fi_av_xfer
%attr(755,root,root) %{_bindir}/fi_bw
%attr(755,root,root) %{_bindir}/fi_dgram_pingpong
%attr(755,root,root) %{_bindir}/fi_efa_info_test
%attr(755,root,root) %{_bindir}/fi_efa_rnr_queue_resend
%attr(755,root,root) %{_bindir}/fi_efa_rnr_read_cq_error
%attr(755,root,root) %{_bindir}/fi_loopback
%attr(755,root,root) %{_bindir}/fi_mcast
%attr(755,root,root) %{_bindir}/fi_msg_bw
%attr(755,root,root) %{_bindir}/fi_msg_inject
%attr(755,root,root) %{_bindir}/fi_msg_pingpong
%attr(755,root,root) %{_bindir}/fi_multi_ep
%attr(755,root,root) %{_bindir}/fi_multi_mr
%attr(755,root,root) %{_bindir}/fi_multi_recv
%attr(755,root,root) %{_bindir}/fi_multinode
%attr(755,root,root) %{_bindir}/fi_multinode_coll
%attr(755,root,root) %{_bindir}/fi_rdm_cntr_pingpong
%attr(755,root,root) %{_bindir}/fi_rdm_deferred_wq
%attr(755,root,root) %{_bindir}/fi_rdm_multi_client
%attr(755,root,root) %{_bindir}/fi_rdm_multi_domain
%attr(755,root,root) %{_bindir}/fi_rdm_pingpong
%attr(755,root,root) %{_bindir}/fi_rdm_shared_av
%attr(755,root,root) %{_bindir}/fi_rdm_tagged_bw
%attr(755,root,root) %{_bindir}/fi_rdm_tagged_pingpong
%attr(755,root,root) %{_bindir}/fi_recv_cancel
%attr(755,root,root) %{_bindir}/fi_resmgmt_test
%attr(755,root,root) %{_bindir}/fi_rma_bw
%attr(755,root,root) %{_bindir}/fi_stream_msg
%attr(755,root,root) %{_bindir}/fi_ubertest
%attr(755,root,root) %{_bindir}/fi_unexpected_msg
%attr(755,root,root) %{_bindir}/fi_unmap_mem
%attr(755,root,root) %{_bindir}/rft_yaml_to_junit_xml
%attr(755,root,root) %{_bindir}/runfabtests.py
%{_datadir}/fabtests
%{_mandir}/man1/fi_av_xfer.1*
%{_mandir}/man1/fi_bw.1*
%{_mandir}/man1/fi_dgram_pingpong.1*
%{_mandir}/man1/fi_efa_rnr_queue_resend.1*
%{_mandir}/man1/fi_mcast.1*
%{_mandir}/man1/fi_multi_ep.1*
%{_mandir}/man1/fi_multi_mr.1*
%{_mandir}/man1/fi_multi_recv.1*
%{_mandir}/man1/fi_msg_bw.1*
%{_mandir}/man1/fi_msg_inject.1*
%{_mandir}/man1/fi_msg_pingpong.1*
%{_mandir}/man1/fi_rdm_cntr_pingpong.1*
%{_mandir}/man1/fi_rdm_deferred_wq.1*
%{_mandir}/man1/fi_rdm_multi_client.1*
%{_mandir}/man1/fi_rdm_multi_domain.1*
%{_mandir}/man1/fi_rdm_pingpong.1*
%{_mandir}/man1/fi_rdm_shared_av.1*
%{_mandir}/man1/fi_rdm_tagged_bw.1*
%{_mandir}/man1/fi_rdm_tagged_pingpong.1*
%{_mandir}/man1/fi_recv_cancel.1*
%{_mandir}/man1/fi_resmgmt_test.1*
%{_mandir}/man1/fi_rma_bw.1*
%{_mandir}/man1/fi_ubertest.1*
%{_mandir}/man1/fi_unexpected_msg.1*
%{_mandir}/man1/fi_unmap_mem.1*
%{_mandir}/man7/fabtests.7*
