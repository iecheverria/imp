\brief Distribute IMP tasks to multiple processors or machines.

This module employs a manager-worker model; the main (manager) IMP process
sends the tasks out to one or more workers. Tasks cannot communicate with each
other, but return results to the manager. The manager can then start new tasks,
possibly using results returned from completed tasks. The system is fault
tolerant; if a worker fails, any tasks running on that worker are automatically
moved to another worker.

To use the module, first create a \link IMP::parallel::Manager Manager\endlink
object. Add one or more workers to the Manager using its
\link IMP::parallel::Manager.add_worker() add_worker()\endlink method (example workers are
\link IMP::parallel::LocalWorker LocalWorker\endlink, which simply starts another
IMP process on the same machine as the manager, and
\link IMP::parallel::SGEQsubWorkerArray SGEQsubWorkerArray\endlink, which starts
an array of multiple workers on a Sun GridEngine cluster). Next, call the
\link IMP::parallel::Manager.get_context() get_context()\endlink
method, which creates and returns a new
\link IMP::parallel::Context Context\endlink object.
Add tasks to the Context with the
\link IMP::parallel::Context.add_task() Context.add_task()\endlink method
(each task is
simply a Python function or other callable object). Finally, call
\link IMP::parallel::Context.get_results_unordered() Context.get_results_unordered()\endlink to
send the tasks out to the workers (a worker only runs a single task at a time;
if there are more tasks than workers later tasks will be queued until a worker
is done with an earlier task). This method returns the results from each task
as it completes.

Setup in IMP is often expensive, and thus the Manager.get_context() method
allows you to specify a Python function or other callable object to do any
setup for the tasks. This function will be run on the worker before any tasks
from that context are started (the return values from this function are
passed to the task functions). If multiple tasks from the same context are
run on the same worker, the setup function is only called once.

<b>Troubleshooting</b>

Several common problems with this module are described below, together with
solutions.

 - <b>Master process fails with <tt>/bin/sh: qsub: command not found</tt>,
   but <tt>qsub</tt> works fine from a terminal.</b>\n
   SGEQsubWorkerArray uses the <tt>qsub</tt> command to submit the SGE job that
   starts the workers. Thus, <tt>qsub</tt> must be in your system PATH. This may
   not be the case if you are using a shell script such as <tt>imppy.sh</tt>
   to start IMP. To fix this, modify the shell script to add the directory
   containing <tt>qsub</tt> to the PATH, or remove the setting of PATH entirely.

 - <b>The manager process 'hangs' and does not do anything when
   Context.get_results_unordered() is called.</b>\n
   Usually this is because no workers have successfully started up. Check the
   worker output files to determine what the problem is.

 - <b>%Worker output files contain only a Python traceback ending in
   <tt>ImportError: No module named IMP.parallel.worker_handler</tt>.</b>\n
   The workers simply run 'python' and expect to be able to load in the IMP
   Python modules. If you need to run a modified version of Python, or usually
   prefix your Python command with a shell script such as <tt>imppy.sh</tt>,
   you need to tell the workers to do that too. Specify the full command line
   needed to start a suitable Python interpreter as the 'python' argument when
   you create the Manager object.

 - <b>%Worker output files contain only a Python traceback ending in
   <tt>socket.error: (110, 'Connection timed out')</tt>.</b>\n
   The workers need to connect to the machine running the manager process
   over the network. This connection can fail (or time out) if that machine
   is firewalled. It can also fail if the manager machine is multi-homed (a
   common setup for the headnode of a compute cluster). For a multi-homed
   manager machine, use the 'host' argument when you create the Manager object
   to tell the workers the name of the machine as visible to them (typically
   this is the name of the machine's internal network interface).

 - <b>%Worker output files contain only a Python traceback ending in
   <tt>socket.error: (111, 'Connection refused')</tt>.</b>\n
   If the manager encounters an error and exits, it will no longer be around
   to accept connections from workers, so they will get this error when they
   try to start up. Check the manager log file for errors. Alternatively, the
   manager may have simply finished all of its work and exited normally before
   the worker started (either the manager had little work to do, or the worker
   took a very long time to start up). This is normal.

# Info

_Author(s)_: Ben Webb

_Maintainer_: `benmwebb`

_License_: [LGPL](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Publications_:
 - See [main IMP papers list](@ref publications).
